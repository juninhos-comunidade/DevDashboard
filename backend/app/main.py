from fastapi import FastAPI
from sqlalchemy import text
from app.database.criar_database import engine

app = FastAPI()

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
    
