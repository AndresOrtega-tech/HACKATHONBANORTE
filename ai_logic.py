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

def generate_learning_path(answers: List[int]) -> Dict[str, List[str]]:
    """Generar la ruta de aprendizaje basada en las respuestas de la encuesta."""
    # Preprocesar las respuestas
    X = np.array([answers])
    predictions = model.predict(X)

    # Umbral para las predicciones
    threshold = 0.5
    learning_paths = {}

    # Aquí suponemos que tienes un mapeo de índices a nombres de módulos
    for i, predicted in enumerate(predictions[0]):
        if predicted > threshold:
            path_name = list(content_map.keys())[i]
            # Obtener el contenido de cada ruta desde content_map
            learning_paths[path_name] = content_map[path_name]["resources"]

    # Seleccionar los tres módulos más relevantes
    sorted_paths = sorted(learning_paths.items(), key=lambda x: predictions[0][list(content_map.keys()).index(x[0])], reverse=True)
    
    # Tomar solo los primeros 3 módulos o menos si no hay suficientes
    top_learning_paths = dict(sorted_paths[:3])

    # Si hay menos de 3, completar con módulos aleatorios de content_map
    while len(top_learning_paths) < 3:
        remaining_modules = set(content_map.keys()) - set(top_learning_paths.keys())
        if remaining_modules:
            random_module = np.random.choice(list(remaining_modules))
            top_learning_paths[random_module] = content_map[random_module]["resources"]

    return top_learning_paths


# Referencias a las colecciones
learning_paths_ref = db.collection('learning_paths')


def get_learning_path(username: str, answers: List[int]) -> Dict[str, List[str]]:
    """Genera un camino de aprendizaje basado en el usuario desde la base de datos y lo almacena en Firestore."""
    
    # Generar la ruta de aprendizaje basada en las respuestas de la encuesta
    learning_modules = generate_learning_path(answers)

    # Almacenar el camino de aprendizaje en la colección learning_paths
    learning_paths_ref.document(username).set({
        'learning_path': learning_modules,
        'started': False  # O lo que necesites según tu lógica
    })
    
    return {
        'modules': learning_modules
    }


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
