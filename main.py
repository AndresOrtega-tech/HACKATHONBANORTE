from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Union
from ai_logic import generate_learning_path, recommend_products, get_personalized_news

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

class Product(BaseModel):
    id: str
    name: str
    description: str

class News(BaseModel):
    id: str
    title: str
    content: str

# --- In-Memory Data Storage ---
users_db: Dict[str, str] = {}
survey_responses: Dict[str, List[int]] = {}
learning_paths: Dict[str, LearningPath] = {}
chatbot_history: Dict[str, List[Dict[str, Union[str, str]]]] = {}

# Base de datos de contenido
content_db: Dict[str, Dict[str, Union[str, List[str]]]] = {
    "basic_finance": {"question": "¿Conoces los conceptos básicos de finanzas personales?",
                      "resources": ["Introducción a Finanzas Personales", "Presupuesto Básico", "Ahorro vs. Inversión"]},
    "investment": {"question": "¿Sabes cómo funciona la inversión en acciones?",
                   "resources": ["Introducción a Inversiones", "Tipos de Inversiones", "Riesgo y Rendimiento"]},
    "budgeting": {"question": "¿Tienes experiencia creando un presupuesto?",
                  "resources": ["Cómo Crear un Presupuesto", "Control de Gastos", "Herramientas para Presupuesto"]},
    "debt_management": {"question": "¿Sabes cómo manejar deudas eficientemente?",
                        "resources": ["Tipos de Deudas", "Estrategias de Pago de Deudas", "Crédito Inteligente"]}
}

# Productos y Noticias Personalizados para Usuarios
user_products: Dict[str, List[Product]] = {
    "usuario1": [
        Product(id="prod1", name="Cuenta de Ahorro Banorte", description="Una cuenta de ahorro con beneficios exclusivos para clientes."),
        Product(id="prod2", name="Tarjeta de Crédito Oro", description="Tarjeta de crédito con puntos Banorte y tasa preferencial."),
        Product(id="prod3", name="Seguro de Vida", description="Cobertura completa con beneficios de salud y vida.")
    ]
}

user_news: Dict[str, List[News]] = {
    "usuario1": [
        News(id="news1", title="Nueva Ley de Inversión", content="El gobierno ha implementado nuevas regulaciones para proteger a los inversores."),
        News(id="news2", title="Consejos de Ahorro", content="Expertos recomiendan un nuevo enfoque para ahorrar en tiempos de inflación."),
        News(id="news3", title="Mercado Financiero 2024", content="Las proyecciones del mercado financiero para 2024 son optimistas.")
    ]
}

# --- API Routes ---
api_router = APIRouter()

@api_router.get("/")
def read_root():
    return {"message": "Bienvenido a la plataforma de crecimiento financiero Hackathon Banorte"}

@api_router.post('/register')
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail='Username already registered')
    users_db[user.username] = user.password
    return {'message': 'User registered successfully'}

@api_router.post('/login')
async def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    return {'message': 'Login successful'}

@api_router.post("/survey")
async def submit_survey(response: SurveyResponse):
    if len(response.answers) != 7:
        raise HTTPException(status_code=400, detail="Survey must contain 7 answers")
    survey_responses[response.username] = response.answers
    return {"message": "Survey responses updated!"}

@api_router.get("/learning-path/{username}")
async def get_learning_path(username: str):
    # Usa la función importada para generar la ruta de aprendizaje
    path = generate_learning_path(username)
    return {"username": username, "learning_path": path}

@api_router.post("/chatbot")
async def chatbot_interact(query: ChatBotQuery):
    if query.username not in users_db:
        raise HTTPException(status_code=404, detail='User not found')
    user_message = query.message
    bot_response = f"Hola {query.username}, aquí tienes algunos consejos financieros sobre: {user_message}"
    if query.username not in chatbot_history:
        chatbot_history[query.username] = []
    chatbot_history[query.username].append({"user": user_message, "bot": bot_response})
    return {"user_message": user_message, "bot_response": bot_response}

@api_router.get("/dashboard/{username}")
async def get_dashboard(username: str):
    if username not in users_db:
        raise HTTPException(status_code=404, detail='User not found')
    learning_path = learning_paths.get(username)
    learning_path_data = learning_path.path if learning_path else "No learning path"
    user_data = {
        "survey_responses": survey_responses.get(username, "No survey data"),
        "learning_path": learning_path_data,
        "chatbot_history": chatbot_history.get(username, []),
        "products": user_products.get(username, []),
        "news": user_news.get(username, [])
    }
    return {"username": username, "dashboard": user_data}

@api_router.get("/products/{username}")
async def get_products(username: str):
    # Usa la función importada para obtener productos personalizados
    products = recommend_products(username)
    return {"username": username, "products": products}

@api_router.get("/news/{username}")
async def get_news(username: str):
    # Usa la función importada para obtener noticias personalizadas
    news = get_personalized_news(username)
    return {"username": username, "news": news}

# --- Mount the API Router ---
app.include_router(api_router)