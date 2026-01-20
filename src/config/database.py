import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env que está na raiz
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Conexão com PostgreSQL realizada com sucesso!")
        
except SQLAlchemyError as e:
    print(f"Erro ao conectar ao banco: {e}")