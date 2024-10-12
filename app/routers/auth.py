from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

# Diccionario temporal para almacenar usuarios y contraseñas
users_db : Dict[str, str] = {}

class User(BaseModel):
    username: str
    password: str

@router.post('/register')
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail='Username already registered')
    
    # Guardar usuario
    users_db[user.username] = user.password
    return {'message': 'User registered successfully'}

@router.post('/login')
async def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    
    return {'message': 'Login successful'}