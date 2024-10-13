# chatbot.py

from transformers import pipeline

# Cargar el modelo de chatbot (reemplaza el modelo según sea necesario)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def generate_chatbot_response(user_message: str) -> str:
    response = chatbot(user_message)[0]['generated_text']
    return response