from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Union
import random
from database import *
from database import get_user_contract_products



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes, puedes especificar dominios aquí
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)

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

class Product(BaseModel):
    id: str
    name: str
    description: str

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
    
    # Guardar las respuestas de la encuesta
    add_survey_response(response.username, response.answers)
    
    # Generar la ruta de aprendizaje
    set_learning_path(response.username)  # Llama a la función que genera la ruta de aprendizaje
    
    return {"message": "Survey responses updated and learning path generated!"}

@api_router.get("/learning-path/{username}")
async def get_learning_path_route(username: str):
    path_info = get_learning_path(username)
    if not path_info:
        set_learning_path(username)  # Genera la ruta si no existe
        path_info = get_learning_path(username)
    
    return {
        "username": username,
        "learning_path": path_info['learning_path'],
        "started": path_info['started']  # Incluye si ya ha comenzado
    }

@api_router.post("/chatbot")
async def chatbot_interact(query: ChatBotQuery):
    if not get_user(query.username):
        raise HTTPException(status_code=404, detail='User not found')

    user_message = query.message.lower()
    bot_response = ""

    # Check for keywords and customize responses
    if "noticia" in user_message:
        news = get_user_news(query.username)
        if not news:
            bot_response = "No hay noticias disponibles."
        else:
            random_news = random.sample(news, min(3, len(news)))
            bot_response = "Aquí tienes algunas noticias financieras:\n" + "\n".join(random_news)

    elif "contenido" in user_message:
        learning_path_data = get_learning_path(query.username)
        if learning_path_data:
            bot_response = f"Tienes estos temas en tu ruta de aprendizaje: {', '.join(learning_path_data['learning_path'])}."
        else:
            bot_response = "No tienes una ruta de aprendizaje establecida."

    elif "producto" in user_message:
        contracted_products = get_user_contract_products(query.username)
        if contracted_products:
            product_names = ", ".join([product.name for product in contracted_products])
            bot_response = f"Tienes los siguientes productos contratados: {product_names}."
        else:
            bot_response = "No tienes productos contratados registrados."

    else:
        # Default response if no keyword is matched
        bot_response = f"Hola {query.username}, aquí tienes algunos consejos financieros sobre: {user_message}"

    # Save the conversation to the chatbot history
    add_chatbot_message(query.username, user_message, bot_response)

    return {"user_message": query.message, "bot_response": bot_response}

    add_chatbot_message(query.username, user_message, bot_response)
    return {"user_message": query.message, "bot_response": bot_response}

    add_chatbot_message(query.username, user_message, bot_response)
    return {"user_message": user_message, "bot_response": bot_response}

def generate_financial_response(message: str, username: str) -> str:
    """Genera una respuesta financiera basada en la base de datos."""
    
    # Lógica simple para identificar palabras clave en el mensaje
    if "producto" in message.lower():
        products = get_user_products(username)
        if products:
            return f"Aquí están tus productos: {', '.join(products)}."
        else:
            return "No tienes productos registrados."

    elif "noticia" in message.lower():
        news = get_user_news(username)
        if news:
            return f"Aquí tienes las últimas noticias: {', '.join(news)}."
        else:
            return "No hay noticias disponibles."

    elif "contenido" in message.lower():
        learning_path_data = get_learning_path(username)
        if learning_path_data:
            return f"Tienes estos temas en tu ruta de aprendizaje: {', '.join(learning_path_data['learning_path'])}."
        else:
            return "No tienes una ruta de aprendizaje establecida."

    else:
        return "Lo siento, no entiendo tu solicitud. ¿Puedes preguntar sobre productos, noticias o contenido?"

@api_router.get("/dashboard/{username}")
async def get_dashboard(username: str):
    # Check if the user exists
    if not get_user(username):
        raise HTTPException(status_code=404, detail='User not found')

    # Fetch the necessary data for the dashboard
    survey_data = get_survey_response(username)
    learning_path_data = get_learning_path(username)
    chatbot_history_data = get_chatbot_history(username)
    products = get_user_contract_products(username)  # Fetch products
    news = get_user_news(username)

    # Prepare the user data to be returned
    user_data = {
        "survey_responses": survey_data or "No survey data",
        "learning_path": learning_path_data or "No learning path",
        "chatbot_history": chatbot_history_data,
        "products": products or "No products",  # Return products as a list of dicts
        "news": news
    }

    # Return the dashboard data
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


@api_router.post("/add-products/{username}")
async def add_products(username: str, products: List[Product]):
    """Agrega una lista de productos a un usuario específico."""
    if not get_user(username):
        raise HTTPException(status_code=404, detail='User not found')
    
    # Corrected function call
    add_user_contract_products(username, products)
    return {"message": f"Products added successfully for user {username}"}


# --- Mount the API Router ---
app.include_router(api_router)