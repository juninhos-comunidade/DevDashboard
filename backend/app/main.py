'''from fastapi import FastAPI
from sqlalchemy import text
from app.database.criar_database import engine
from app.database.base import Base

from app.models.user_models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"teste": "ok"}


@app.get("/health/db")
def health_db():
    try:
        with engine.connect() as con:
            con.execute(text("SELECT 1"))

        return {
            "status": "Banco de dados conectado"
        }    

    except Exception as e:
        return {
            "status": "Banco de dados disconectado",
            "Erro": str(e)
        }
   '''
from app.routers.auth import router
from fastapi import FastAPI
from app.database.base import Base
from app.database.criar_database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)

