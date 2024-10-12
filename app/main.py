from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la plataforma de crecimiento financiero Hackathon Banorte."}
users_db : Dict[str, str] = {}

class User(BaseModel):
    username: str
    password: str

@app.post('/register')
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail='Username already registered')
    
    # Guardar usuario
    users_db[user.username] = user.password
    return {'message': 'User registered successfully'}

@app.post('/login')
async def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    
    return {'message': 'Login successful'}

survey_responses: Dict[str, int] = {}

class SurveyResponse(BaseModel):
    username: str
    score: int

# Simulación de respuestas de encuesta
survey_responses = []

@app.post("/survey")
async def submit_survey(response: dict):
    survey_responses.append(response)
    return {"message": "Survey response received!"}
