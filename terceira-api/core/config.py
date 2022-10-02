import os
from dotenv import load_dotenv
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

class Settings(BaseSettings):
    # CONFIGURAÇÕES GERAIS DA APLICAÇÃO

    API_V1_STR: str = "/api/v1"                                                     # Rota da API
    PROJECT_NAME: str = "FastAPI"                                                   # Nome do projeto
    DB_URL: str = os.getenv("DB_URL")                                               # URL do banco de dados
    DBBaseModel: declarative_base() = declarative_base()                          # Modelo base do banco de dados

    class Config:
        case_sensitive = True                                                       # Configurações sensíveis ao caso


settings = Settings()                                                              # Instância das configurações