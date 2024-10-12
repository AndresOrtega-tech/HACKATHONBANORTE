from typing import List, Dict, Optional
from ai_logic import generate_learning_path, recommend_products, get_personalized_news
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    id: str
    name: str
    description: str

class News(BaseModel):
    id: str
    title: str
    content: str

# Base de datos simulada
users_db: Dict[str, str] = {}
survey_responses: Dict[str, List[int]] = {}
learning_paths: Dict[str, List[str]] = {}
user_products: Dict[str, List[Product]] = {}
user_news: Dict[str, List[News]] = {}
chatbot_history: Dict[str, List[Dict[str, str]]] = {}

def add_user(username: str, password: str):
    users_db[username] = password

def get_user(username: str) -> Optional[str]:
    return users_db.get(username)

def add_survey_response(username: str, answers: List[int]):
    survey_responses[username] = answers

def get_survey_response(username: str) -> Optional[List[int]]:
    return survey_responses.get(username)

def set_learning_path(username: str):
    learning_paths[username] = generate_learning_path(username)

def get_learning_path(username: str) -> Optional[List[str]]:
    return learning_paths.get(username)

def set_user_products(username: str):
    user_products[username] = recommend_products(username)

def get_user_products(username: str) -> List[Product]:
    return user_products.get(username, [])

def set_user_news(username: str):
    user_news[username] = get_personalized_news(username)

def get_user_news(username: str) -> List[News]:
    return user_news.get(username, [])

def add_chatbot_message(username: str, user_message: str, bot_response: str):
    if username not in chatbot_history:
        chatbot_history[username] = []
    chatbot_history[username].append({"user": user_message, "bot": bot_response})

def get_chatbot_history(username: str) -> List[Dict[str, str]]:
    return chatbot_history.get(username, [])
