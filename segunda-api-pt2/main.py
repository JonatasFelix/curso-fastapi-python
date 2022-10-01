from fastapi import FastAPI             # IMPORTANDO A CLASSE FastAPI - PARA CRIAR A APLICAÇÃO

from routes import curso_router         # IMPORTANDO O ARQUIVO curso_router.py
from routes import usuario_router       # IMPORTANDO O ARQUIVO usuario_router.py

app = FastAPI(                          # INSTANCIANDO A CLASSE FastAPI - PARA CRIAR A APLICAÇÃO
    title="API COM ROTAS",              # TÍTULO DA APLICAÇÃO
    description="API COM ROTAS",        # DESCRIÇÃO DA APLICAÇÃO
    version="1.0.0"                     # VERSÃO DA APLICAÇÃO
)                         

app.include_router(curso_router.router, tags=["curos"])         # INCLUINDO A ROTA DE CURSOS - TAGS PARA ORGANIZAR AS ROTAS NA DOCUMENTAÇÃO
app.include_router(usuario_router.router, tags=["usuarios"])    # INCLUINDO A ROTA DE USUARIOS - TAGS PARA ORGANIZAR AS ROTAS NA DOCUMENTAÇÃO


# RODANDO A APLICAÇÃO
# python main.py

if __name__ == "__main__":            # VERIFICANDO SE O ARQUIVO É O PRINCIPAL

    import uvicorn      # IMPORTANDO A BIBLIOTECA uvicorn - PARA RODAR A APLICAÇÃO

    uvicorn.run(
        "main:app",         # ARQUIVO:CLASSE
        host="0.0.0.0",     # ENDERÇO ONDE A APLICAÇÃO VAI RODAR
        port=8000,          # PORTA ONDE A APLICAÇÃO VAI RODAR
        debug=True,         # MODO DEBUG
        reload=True         # RECARREGAR A APLICAÇÃO QUANDO HOUVER ALTERAÇÃO NO CÓDIGO
    )