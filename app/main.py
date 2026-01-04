# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import clientes

app = FastAPI(
    title="API de Clientes",
    version="1.0.0"
)

# CORS (pensando en React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción se ajusta
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)


@app.get("/")
def root():
    return {
        "mensaje": "API de Clientes activa 🚀"
    }
