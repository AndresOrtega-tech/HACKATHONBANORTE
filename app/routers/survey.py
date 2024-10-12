from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

# Diccionario temporal para almacenar las respuestas de la encuesta
survey_responses: Dict[str, int] = {}

class SurveyResponse(BaseModel):
    username: str
    score: int

# Simulación de respuestas de encuesta
survey_responses = []

@router.post("/survey")
async def submit_survey(response: dict):
    survey_responses.append(response)
    return {"message": "Survey response received!"}
