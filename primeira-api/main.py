from fastapi import FastAPI  # IMPORTANDO A CLASSE FastAPI

app = FastAPI()  # INSTANCIANDO A CLASSE FastAPI


@app.get("/")  # DECORATOR
async def raiz(): # FUNÇÃO QUE SERÁ EXECUTADA QUANDO O USUÁRIO ACESSAR A RAIZ DO SITE
    return {"message": "Hello World"}  # DICIONÁRIO === OBJETO EM JS


if __name__ == "__main__":  # SE O ARQUIVO FOR EXECUTADO DIRETAMENTE
    import uvicorn

    uvicorn.run(
        "main:app",         # ARQUIVO:VARIAVEL QUE VAI SER EXECUTADA
        host="127.0.0.1",   # ENDEEREÇO DO SERVIDOR  #0.0.0.0 TODOS DA REDE PASSAM A TER ACESSO
        port=8000,          # PORTA DO SERVIDOR
        log_level="info",   # NIVEL DE LOG
        reload=True         # RECARREGA O SERVIDOR A CADA ALTERAÇÃO
    )
