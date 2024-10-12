from fastapi import APIRouter
from typing import Dict

router = APIRouter()

# Diccionario temporal para almacenar rutas de aprendizaje
learning_paths: Dict[str, str] = {}

@router.get("/learning-path/{username}")
def get_learning_path(username: str):
    # Aquí puedes implementar la lógica de IA para generar rutas de aprendizaje
    if username in learning_paths:
        return {"learning_path": learning_paths[username]}
    
    return {"message": "No se encontró una ruta de aprendizaje para este usuario."}
