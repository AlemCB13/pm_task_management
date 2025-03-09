from fastapi import FastAPI
from .endpoints import tasks  # Importa los endpoints de tasks.py
from .database import engine, Base  # Importa la configuración de la base de datos

# Crea la aplicación FastAPI
app = FastAPI()

# Crea las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Incluye los endpoints de tasks.py
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

# Ruta de inicio (opcional)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management Service!"}