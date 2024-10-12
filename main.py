from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Union
from database import add_user, get_user, add_survey_response, get_survey_response, set_learning_path, get_learning_path
from database import set_user_products, get_user_products, set_user_news, get_user_news, add_chatbot_message, get_chatbot_history

app = FastAPI()

# --- Models ---
class User(BaseModel):
    username: str
    password: str

class SurveyResponse(BaseModel):
    username: str
    answers: List[int]

class LearningPath(BaseModel):
    username: str
    path: List[str]

class ChatBotQuery(BaseModel):
    username: str
    message: str

# --- API Routes ---
api_router = APIRouter()

@api_router.get("/")
def read_root():
    return {"message": "Bienvenido a la plataforma de crecimiento financiero Hackathon Banorte"}

@api_router.post('/register')
async def register(user: User):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail='Username already registered')
    add_user(user.username, user.password)
    return {'message': 'User registered successfully'}

@api_router.post('/login')
async def login(user: User):
    if not get_user(user.username) or get_user(user.username) != user.password:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    return {'message': 'Login successful'}

@api_router.post("/survey")
async def submit_survey(response: SurveyResponse):
    if len(response.answers) != 7:
        raise HTTPException(status_code=400, detail="Survey must contain 7 answers")
    add_survey_response(response.username, response.answers)
    return {"message": "Survey responses updated!"}

@api_router.get("/learning-path/{username}")
async def get_learning_path_route(username: str):
    path = get_learning_path(username)
    if not path:
        set_learning_path(username)
        path = get_learning_path(username)
    return {"username": username, "learning_path": path}

@api_router.post("/chatbot")
async def chatbot_interact(query: ChatBotQuery):
    if not get_user(query.username):
        raise HTTPException(status_code=404, detail='User not found')
    user_message = query.message
    bot_response = f"Hola {query.username}, aquí tienes algunos consejos financieros sobre: {user_message}"
    add_chatbot_message(query.username, user_message, bot_response)
    return {"user_message": user_message, "bot_response": bot_response}

@api_router.get("/dashboard/{username}")
async def get_dashboard(username: str):
    if not get_user(username):
        raise HTTPException(status_code=404, detail='User not found')

    survey_data = get_survey_response(username)
    learning_path_data = get_learning_path(username)
    chatbot_history_data = get_chatbot_history(username)
    products = get_user_products(username)
    news = get_user_news(username)

    user_data = {
        "survey_responses": survey_data or "No survey data",
        "learning_path": learning_path_data or "No learning path",
        "chatbot_history": chatbot_history_data,
        "products": products,
        "news": news
    }
    return {"username": username, "dashboard": user_data}

@api_router.get("/products/{username}")
async def get_products(username: str):
    set_user_products(username)
    products = get_user_products(username)
    return {"username": username, "products": products}

@api_router.get("/news/{username}")
async def get_news(username: str):
    set_user_news(username)
    news = get_user_news(username)
    return {"username": username, "news": news}

# --- Mount the API Router ---
app.include_router(api_router)
