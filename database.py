from typing import List, Dict, Optional, Union
from ai_logic import generate_learning_path, recommend_products, get_personalized_news
from pydantic import BaseModel
from google.cloud import firestore

# Inicializar Firestore
db = firestore.Client(project='gcp-banorte-hackaton-team-13')

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

# Referencias a las colecciones
users_ref = db.collection('users')
survey_responses_ref = db.collection('survey_responses')
learning_paths_ref = db.collection('learning_paths')
user_products_ref = db.collection('user_products')
user_news_ref = db.collection('user_news')
chatbot_history_ref = db.collection('chatbot_history')
modules_ref = db.collection('content_topics')
chatbot_messages = db.collection('chatbot_messages')


def add_user(username: str, password: str):
    """Agregar un nuevo usuario a Firestore."""
    try:
        # Crear una referencia al documento del usuario
        users_ref.document(username).set({
            'username': username,
            'password': password
        })
        print(f"Usuario {username} agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar usuario: {e}")

def get_user(username: str) -> Optional[str]:
    """Obtener la contraseña de un usuario dado su nombre de usuario."""
    try:
        user_doc = users_ref.document(username).get()
        return user_doc.to_dict().get('password') if user_doc.exists else None
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return None

def add_survey_response(username: str, answers: List[int]):
    """Agregar las respuestas de una encuesta para un usuario."""
    try:
        survey_responses_ref.document(username).set({
            'answers': answers
        })
        print(f"Respuestas de la encuesta para {username} agregadas correctamente.")
    except Exception as e:
        print(f"Error al agregar respuestas de la encuesta: {e}")

def get_survey_response(username: str) -> Optional[List[int]]:
    """Obtener las respuestas de la encuesta de un usuario."""
    try:
        response_doc = survey_responses_ref.document(username).get()
        return response_doc.to_dict().get('answers') if response_doc.exists else None
    except Exception as e:
        print(f"Error al obtener respuestas de la encuesta: {e}")
        return None

def set_learning_path(username: str):
    """Establecer el camino de aprendizaje para un usuario."""
    try:
        # Obtener las respuestas de la encuesta del usuario
        answers = get_survey_response(username)
        if not answers:
            print(f"No se encontraron respuestas de la encuesta para {username}.")
            return
        
        # Generar la ruta de aprendizaje basada en las respuestas de la encuesta
        learning_path = generate_learning_path(answers)
        
        # Almacenar el camino de aprendizaje en Firestore
        learning_paths_ref.document(username).set({
            'learning_path': learning_path
        })
        print(f"Camino de aprendizaje para {username} establecido correctamente.")
    except Exception as e:
        print(f"Error al establecer el camino de aprendizaje: {e}")


def get_learning_path(username: str) -> Optional[Dict[str, Union[Dict[str, List[str]], bool]]]:
    """Obtener el camino de aprendizaje de un usuario."""
    try:
        path_doc = learning_paths_ref.document(username).get()
        if path_doc.exists:
            data = path_doc.to_dict()
            return {
                'learning_path': data.get('learning_path'),
                'started': data.get('started', False)  # Devuelve el estado 'started'
            }
        else:
            print(f"No se encontró un camino de aprendizaje para el usuario: {username}")
            return None
    except Exception as e:
        print(f"Error al obtener el camino de aprendizaje: {e}")
        return None
    
def set_user_products(username: str):
    """Establecer productos recomendados para un usuario."""
    try:
        products = recommend_products(username)
        user_products_ref.document(username).set({
            'products': [product.dict() for product in products]
        })
        print(f"Productos recomendados para {username} establecidos correctamente.")
    except Exception as e:
        print(f"Error al establecer productos recomendados: {e}")

def get_user_products(username: str) -> List[Product]:
    """Obtener productos recomendados de un usuario."""
    try:
        products_doc = user_products_ref.document(username).get()
        if products_doc.exists:
            products_data = products_doc.to_dict().get('products', [])
            return [Product(**product) for product in products_data]
        return []
    except Exception as e:
        print(f"Error al obtener productos recomendados: {e}")
        return []

def set_user_news(username: str):
    """Establecer noticias personalizadas para un usuario."""
    try:
        news_list = get_personalized_news(username)
        user_news_ref.document(username).set({
            'news': [news.dict() for news in news_list]
        })
        print(f"Noticias personalizadas para {username} establecidas correctamente.")
    except Exception as e:
        print(f"Error al establecer noticias personalizadas: {e}")

def get_user_news(username: str) -> List[News]:
    """Obtener noticias personalizadas de un usuario."""
    try:
        news_doc = user_news_ref.document(username).get()
        if news_doc.exists:
            news_data = news_doc.to_dict().get('news', [])
            return [News(**news) for news in news_data]
        return []
    except Exception as e:
        print(f"Error al obtener noticias personalizadas: {e}")
        return []

def add_chatbot_message(username: str, user_message: str, bot_response: str):
    """Agregar un mensaje de chatbot a la historia de un usuario."""
    try:
        history_doc = chatbot_history_ref.document(username)
        history_data = history_doc.get().to_dict() if history_doc.get().exists else {'history': []}
        
        history_data['history'].append({"user": user_message, "bot": bot_response})
        history_doc.set(history_data)
        print(f"Mensaje del chatbot agregado a la historia de {username}.")
    except Exception as e:
        print(f"Error al agregar mensaje del chatbot: {e}")

def get_chatbot_history(username: str):
    return chatbot_messages.get(username, [])

def get_user_news(username: str) -> List[str]:
    # Obtener la colección de noticias
    news_ref = db.collection('news_articles')
    
    # Obtener todos los documentos en la colección
    news_docs = news_ref.stream()
    
    # Almacenar el contenido de las noticias en una lista
    news = []
    for doc in news_docs:
        news.append(doc.to_dict()['content'])
    
    return news

