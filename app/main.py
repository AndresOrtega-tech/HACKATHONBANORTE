from fastapi import FastAPI
from routers import auth, survey, learning  # Asegúrate de que esto esté correcto

app = FastAPI()

# Incluye los routers
app.include_router(auth.router)
app.include_router(survey.router)
app.include_router(learning.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la plataforma de crecimiento financiero."}

