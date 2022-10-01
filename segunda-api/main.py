from fastapi import FastAPI 
from fastapi import HTTPException   # CRIAR EXCEÇÕES
from fastapi import status          # CRIAR STATUS CODES PARA AS EXCEÇÕES

from models import Curso

app = FastAPI() # ESTANCIANDO A CLASSE FastAPI

cursos = { # DICIONÁRIO DE CURSOS (OBJETOS DO JS)
    1: {
        "titulo": "Curso de Python",
        "aulas": 10,
        "horas": 20
    },
    2: {
        "titulo": "Curso de FastAPI",
        "aulas": 10,
        "horas": 20
    },
    3: {
        "titulo": "Curso de Docker",
        "aulas": 10,
        "horas": 20
    }
}

### FAST API TEM TIPAGEM DA MESMA FORMA QUE O TYPESCRIPT

### TYPESCRIPT X PYTHON
###     number x int
###     string x str
###     boolean x bool
###     object x dict
###     array x list


@app.get("/cursos")     # ROTA PARA LISTAR TODOS OS CURSOS
async def get_cursos(): # FUNÇÃO QUE RETORNA TODOS OS CURSOS
    return cursos       # RETORNA TODOS OS CURSOS

@app.get("/cursos/{id}")                                # ROTA PARA LISTAR UM CURSO ESPECÍFICO PELO ID
async def get_curso(id: int):                           # FUNÇÃO QUE RETORNA UM CURSO ESPECÍFICO PELO ID
    try:                                                # TENTA EXECUTAR O CÓDIGO
        curso = cursos[id]                                  # ATUALIZA O DICIONÁRIO COM O ID
        return curso                                        # RETORNA O CURSO ESPECÍFICO PELO ID
    except:                                             # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                # LANÇA UMA EXCEÇÃO 
            status_code=status.HTTP_404_NOT_FOUND,          # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"      # DETALHES DA EXCEÇÃO - MENSAGEM
        )

@app.post("/cursos", status_code=status.HTTP_201_CREATED)   # ROTA PARA CRIAR UM CURSO - STATUS CODE 201 CREATED
async def post_curso(curso: Curso):                         # FUNÇÃO QUE CRIA UM CURSO
    id = len(cursos) + 1                                    # ID DO CURSO
    del curso.id                                            # DELETA O ID DO CURSO - NÃO É NECESSÁRIO POIS O ID É GERADO AUTOMATICAMENTE
    cursos[id] = curso                                      # ADICIONA O CURSO AO DICIONÁRIO
    return cursos[id]                                       # RETORNA O CURSO CRIADO

@app.put("/cursos/{id}", status_code=status.HTTP_202_ACCEPTED)  # ROTA PARA ATUALIZAR UM CURSO - STATUS CODE 202 ACCEPTED
async def put_curso(id: int, curso: Curso):                     # FUNÇÃO QUE ATUALIZA UM CURSO
    if id in cursos:                                            # SE O CURSO EXISTIR
        del curso.id                                                # DELETA O ID DO CURSO - NÃO É NECESSÁRIO JÁ POSSUIMOS O ID
        cursos[id] = curso                                          # ATUALIZA O CURSO
        return cursos[id]                                           # RETORNA O CURSO ATUALIZADO
    else:                                                       # CASO O CURSO NÃO EXISTA
        raise HTTPException(                                        # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                  # STATUS CODE 404 NOT FOUND
            detail=f"Curso com id {id} não encontrado"              # DETALHES DA EXCEÇÃO - MENSAGEM
        )

@app.delete("/cursos/{id}", status_code=status.HTTP_200_OK)                 # ROTA PARA DELETAR UM CURSO - STATUS CODE 204 NO CONTENT
async def delete_curso(id: int):                                            # FUNÇÃO QUE DELETA UM CURSO
    try:                                                                    # TENTA EXECUTAR O CÓDIGO
        del cursos[id]                                                          # DELETA O CURSO PELO ID
        return {"mensagem": f"Curso com id {id} deletado com sucesso"}          # RETORNA A MENSAGEM DE SUCESSO
    except:                                                                 # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                                    # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                              # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"                          # DETALHES DA EXCEÇÃO - MENSAGEM
        )


if __name__ == "__main__":  # SE O ARQUIVO FOR EXECUTADO DIRETAMENTE, EXECUTA O SERVIDOR - python main.py
    import uvicorn
    uvicorn.run(
        "main:app",         # main:app NOME DO ARQUIVO QUE ESTÁ RODANDO: NOME DA INSTÂNCIA DO FASTAPI
        host="0.0.0.0",     # ENDEREÇO DO SERVIDOR
        port=8000,          # PORTA DO SERVIDOR
        debug=True,         # DEBUG MODE ON (DESENVOLVIMENTO)
        reload=True         # RELOAD ON (DESENVOLVIMENTO)
    )
