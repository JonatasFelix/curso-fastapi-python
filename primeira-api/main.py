from fastapi import FastAPI # IMPORTANDO A CLASSE FastAPI

app = FastAPI() # INSTANCIANDO A CLASSE FastAPI


@app.get("/") # DECORATOR
async def raiz():
    return {"message": "Hello World"} # DICIONÁRIO === OBJETO EM JS