from typing import Generator                        # TYPE GENERATOR

from sqlalchemy.ext.asyncio import AsyncSession     # A SESSÃO É A CONEXÃO COM O BANCO DE DADOS

from core.database import Session                   # IMPORTA A SESSÃO DO ARQUIVO DE BANCO DE DADOS

async def get_session() -> Generator:               # FUNÇÃO QUE CRIA A SESSÃO
    session: AsyncSession = Session()               # CRIA A SESSÃO
    try:                                            # TENTA
        yield session                                   # RETORNA A SESSÃO
    finally:                                        # FINALMENTE
        await session.close()                           # FECHA A SESSÃO
