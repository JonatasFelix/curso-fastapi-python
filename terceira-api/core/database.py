from sqlalchemy.orm import sessionmaker  # SESSIONMAKER É A CLASSE QUE CRIA AS SESSÕES - A SESSÃO É A CONEXÃO COM O BANCO DE DADOS
from sqlalchemy.ext.asyncio import create_async_engine # CRIA O MOTOR ASSÍNCRONO DO BANCO DE DADOS
from sqlalchemy.ext.asyncio import AsyncSession # CRIA A SESSÃO ASSÍNCRONA DO BANCO DE DADOS
from sqlalchemy.ext.asyncio import AsyncEngine # CRIA O MOTOR ASSÍNCRONO DO BANCO DE DADOS

from core.config import settings # IMPORTA AS CONFIGURAÇÕES DO ARQUIVO DE CONFIGURAÇÕES


engine: AsyncEngine = create_async_engine(settings.DB_URL) # CRIA O MOTOR ASSÍNCRONO DO BANCO DE DADOS

Session: AsyncSession = sessionmaker(   # CRIA A SESSÃO ASSÍNCRONA DO BANCO DE DADOS
    autocommit=False,                   # AUTOCOMMIT É O COMANDO QUE FAZ O BANCO DE DADOS EXECUTAR O COMANDO SEM PRECISAR DAR O COMMIT  
    autoflush=False,                    # AUTOFUSH É O COMANDO QUE FAZ O BANCO DE DADOS EXECUTAR O COMANDO SEM PRECISAR DAR O FLUSH                        
    expire_on_commit=False,             # EXPIRA AO COMITAR É O COMANDO QUE FAZ O BANCO DE DADOS EXECUTAR O COMANDO SEM PRECISAR DAR O EXPIRA AO COMITAR
    class_=AsyncSession,                # CLASSE ASSÍNCRONA É A CLASSE QUE CRIA A SESSÃO ASSÍNCRONA DO BANCO DE DADOS
    bind=engine,                        # BIND É O COMANDO QUE FAZ O BANCO DE DADOS EXECUTAR O COMANDO SEM PRECISAR DAR O BIND
)