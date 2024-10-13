from typing import Dict, List
import numpy as np
import tensorflow as tf
from google.cloud import firestore
from info import *

# Cargar el modelo de aprendizaje automático
MODEL_PATH = 'learning_path_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Inicializar Firestore
db = firestore.Client(project='gcp-banorte-hackaton-team-13')

def get_learning_paths_from_db() -> Dict[str, List[str]]:
    """Obtener los nombres de las rutas de aprendizaje y su contenido desde Firestore."""
    try:
        # Asumimos que tienes una colección llamada 'content_topics'
        learning_paths_ref = db.collection('content_topics')
        paths = learning_paths_ref.stream()

        # Devolver un diccionario donde la clave es el nombre de la ruta y el valor es el contenido
        return {doc.id: doc.to_dict().get('content', []) for doc in paths}  
    except Exception as e:
        print(f"Error al obtener rutas de aprendizaje: {e}")
        return {}

def generate_learning_path(answers: List[int]) -> Dict[str, List[str]]:
    """Generar la ruta de aprendizaje basada en las respuestas de la encuesta."""
    # Preprocesar las respuestas
    X = np.array([answers])
    predictions = model.predict(X)

    # Umbral para las predicciones
    threshold = 0.5
    learning_paths = {}

    # Iterar sobre las predicciones y construir la ruta de aprendizaje
    for i, predicted in enumerate(predictions[0]):  # Se asume que predictions es de la forma (1, n)
        if predicted > threshold:
            # Aquí asumimos que el índice de la predicción corresponde al índice de las rutas
            path_name = list(content_map.keys())[i]
            # Obtener el contenido de cada ruta desde content_map
            learning_paths[path_name] = content_map[path_name]["resources"]

    return learning_paths 

def recommend_products(username: str) -> List[dict]:
    # Lógica para recomendar productos financieros al usuario
    return [
        {"id": "prod1", "name": "Tarjeta de Crédito Banorte", "description": "Tarjeta de crédito con beneficios."},
        {"id": "prod2", "name": "Cuenta de Ahorro Premium", "description": "Cuenta de ahorro con altas tasas de interés."}
    ]

def get_personalized_news(username: str) -> List[dict]:
    # Lógica para seleccionar noticias relevantes para el usuario
    return [
        {"id": "news1", "title": "Noticias sobre inversiones", "content": "Las mejores oportunidades para invertir."},
        {"id": "news2", "title": "Consejos financieros", "content": "Aprende cómo mejorar tu situación financiera."}
    ]
