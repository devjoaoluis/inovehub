from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Formato: postgresql://usuario:senha@host:porta/nome_banco
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/incubadoraEmpresa"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Conexão com PostgreSQL realizada com sucesso!")
        
except SQLAlchemyError as e:
    print(f"Erro ao conectar ao banco: {e}")