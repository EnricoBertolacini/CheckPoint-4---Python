from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import database

from controller.controller_livro import router as livro_router
from controller.controller_cliente import router as cliente_router


app = FastAPI(
    title="API de Biblioteca",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


database.criar_tabelas()


app.include_router(livro_router)
app.include_router(cliente_router)