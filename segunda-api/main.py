from fastapi import FastAPI 
from fastapi import HTTPException           # CRIAR EXCEÇÕES
from fastapi import status                  # CRIAR STATUS CODES PARA AS EXCEÇÕES
from fastapi import Response                # CRIAR RESPOSTAS
from fastapi import Path                    # CRIAR PATHS - /{id}
from fastapi import Query                   # CRIAR QUERYS - /?id=1
from fastapi import Header                  # CRIAR HEADERS - GERALMENTE USADO PARA AUTENTICAÇÃO

from typing import Optional                 # CRIAR TIPOS DE DADOS

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

@app.get("/cursos/{id}")                                    # ROTA PARA LISTAR UM CURSO ESPECÍFICO PELO ID
async def get_curso(id: int = Path (                        # FUNÇÃO QUE RETORNA UM CURSO ESPECÍFICO PELO ID
    default=None,                                           # VALOR PADRÃO DO ID - CASO NÃO SEJA PASSADO NENHUM ID                                  
    title="O ID do curso",                                  # TÍTULO DO PARÂMETRO
    description="Deve ser um numero inteiro maior que 0",   # DESCRIÇÃO DE COMO DEVE SER O ID
    gt=0                                                    # MAIOR QUE 0
)):                           
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

@app.delete("/cursos/{id}")                                                 # ROTA PARA DELETAR UM CURSO - STATUS CODE 204 NO CONTENT
async def delete_curso(id: int):                                            # FUNÇÃO QUE DELETA UM CURSO
    try:                                                                    # TENTA EXECUTAR O CÓDIGO
        del cursos[id]                                                          # DELETA O CURSO PELO ID
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)            # FORMA QUE DEVERIA SER FEITO - MAS NO FASTAPI ESTÁ BUGADO
        return Response(status_code=status.HTTP_204_NO_CONTENT)                 # RETORNA O STATUS CODE 204 NO CONTENT - PARA CASOS QUE NÃO POSSUEM RETORNO
    except:                                                                 # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                                    # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                              # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"                          # DETALHES DA EXCEÇÃO - MENSAGEM
        )

@app.get("/queryParams", status_code=status.HTTP_200_OK)        # ROTA USANDO QUERY PARAMS - STATUS CODE 200 OK
async def get_queryParams(
    Authorization: str = Header(default=None,                           # HEADER - AUTENTICAÇÃO
                                title="Token de autorização",           # TÍTULO DO HEADER
                                description="Token de autorização",     # DESCRIÇÃO DO HEADER
                                example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
                                ),               
    a: int = Query( default=None,                               # PARÂMETRO A NO QUERY PARAMS - DEFAULT NONE
                    title="Digite o primeiro numero da soma",   # TÍTULO DO PARÂMETRO
                    description="Deve ser um numero inteiro",   # DESCRIÇÃO DO PARÂMETRO
                    example=1                                   # EXEMPLO DO PARÂMETRO
                ), 
    b: int = Query( default=None,                               # PARÂMETRO B NO QUERY PARAMS - DEFAULT NONE
                    title="Digite o segundo numero da soma",    # TÍTULO DO PARÂMETRO
                    description="Deve ser um numero inteiro",   # DESCRIÇÃO DO PARÂMETRO
                    example=2                                   # EXEMPLO DO PARÂMETRO
                ),
    c: Optional[int] = Query(   default=None,                                                    # PARÂMETRO C NO QUERY PARAMS - É OPCIONAL - DEFAULT NONE
                                title="Digite o terceiro numero da soma",                        # TÍTULO DO PARÂMETRO
                                description="Deve ser um numero inteiro ou não ser informado",   # DESCRIÇÃO DO PARÂMETRO
                                example=3                                                        # EXEMPLO DO PARÂMETRO
                            )
            
):
    print(Authorization)                                        # PRINTA O HEADER
    soma = a + b                                                # SOMA A + B
    if c:                                                       # SE C FOR INFORMADO
        soma += c                                                   # SOMA A + B + C
    return {"soma": soma}                                       # RETORNA A SOMA


if __name__ == "__main__":  # SE O ARQUIVO FOR EXECUTADO DIRETAMENTE, EXECUTA O SERVIDOR - python main.py
    import uvicorn
    uvicorn.run(
        "main:app",         # main:app NOME DO ARQUIVO QUE ESTÁ RODANDO: NOME DA INSTÂNCIA DO FASTAPI
        host="0.0.0.0",     # ENDEREÇO DO SERVIDOR
        port=8000,          # PORTA DO SERVIDOR
        debug=True,         # DEBUG MODE ON (DESENVOLVIMENTO)
        reload=True         # RELOAD ON (DESENVOLVIMENTO)
    )
