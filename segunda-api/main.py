from fastapi import FastAPI 
from fastapi import HTTPException                               # CRIAR EXCEÇÕES
from fastapi import status                                      # CRIAR STATUS CODES PARA AS EXCEÇÕES
from fastapi import Response                                    # CRIAR RESPOSTAS
from fastapi import Body                                        # CRIAR CORPO DA REQUISIÇÃO
from fastapi import Path                                        # CRIAR PATHS - /{id}
from fastapi import Query                                       # CRIAR QUERYS - /?id=1
from fastapi import Header                                      # CRIAR HEADERS - GERALMENTE USADO PARA AUTENTICAÇÃO
from fastapi import Depends                                     # CRIAR DEPENDENCIAS

from time import sleep                                          # IMPORTAR FUNÇÃO SLEEP

from typing import Optional, Any, Dict, List                    # CRIAR TIPOS DE DADOS

from models import Curso                                        # IMPORTAR MODELO DE CURSO
from models import cursos                                       # IMPORTAR LISTA DE CURSOS


def fake_db():
    try:
        print("Conectando ao banco de dados")
        sleep(2)
        print("Conectado")
        sleep(1)
    finally:
        print("Desconectando do banco de dados")

app = FastAPI(
    title="API de Cursos",                              # TITULO DA API - APARECE NA DOCUMENTAÇÃO
    description="CURSO GEEK UNIVERSITY - FASTAPI",      # DESCRIÇÃO DA API - APARECE NA DOCUMENTAÇÃO
    version="0.0.1"                                     # VERSÃO DA API - APARECE NA DOCUMENTAÇÃO


) # ESTANCIANDO A CLASSE FastAPI

### FAST API TEM TIPAGEM DA MESMA FORMA QUE O TYPESCRIPT

### TYPESCRIPT X PYTHON
###     number x int
###     string x str
###     boolean x bool
###     object x dict
###     array x list


@app.get("/cursos",                             # ROTA PARA LISTAR TODOS OS CURSOS
    summary="Listar todos os cursos",           # TITULO DA ROTA - APARECE NA DOCUMENTAÇÃO
    description="Listar todos os cursos",       # DESCRIÇÃO DA ROTA - APARECE NA DOCUMENTAÇÃO
    response_description="Lista de cursos",     # DESCRIÇÃO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO - NA PARTE DO STATUS CODE
    response_model=List[Curso],                 # MODELO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    status_code=status.HTTP_200_OK,              # STATUS CODE DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    tags=["Cursos"]                             # TAGS DA ROTA - APARECE NA DOCUMENTAÇÃO
)             
async def get_cursos(                           # FUNÇÃO QUE RETORNA TODOS OS CURSOS
        db: any = Depends(fake_db)              # INJETANDO DEPENDENCIA DA FUNÇÃO fake_db
    ): 
    return cursos                               # RETORNA TODOS OS CURSOS

@app.get("/cursos/{id}",                                        # ROTA PARA LISTAR UM CURSO ESPECÍFICO PELO ID
    summary="Listar um curso específico",                       # TITULO DA ROTA - APARECE NA DOCUMENTAÇÃO
    description="Listar um curso específico",                   # DESCRIÇÃO DA ROTA - APARECE NA DOCUMENTAÇÃO
    response_description="Curso específico",                    # DESCRIÇÃO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO - NA PARTE DO STATUS CODE
    response_model=Curso,                                       # MODELO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    status_code=status.HTTP_200_OK,                             # STATUS CODE DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    tags=["Cursos"]                                             # TAGS DA ROTA - APARECE NA DOCUMENTAÇÃO
)                                       
async def get_curso(                                            # FUNÇÃO QUE RETORNA UM CURSO ESPECÍFICO PELO ID
    id: int = Path (                                            # ID DO CURSO - PATH PARAMETER
        default=None,                                               # VALOR PADRÃO DO ID - CASO NÃO SEJA PASSADO NENHUM ID                                  
        title="O ID do curso",                                      # TÍTULO DO PARÂMETRO
        description="Deve ser um numero inteiro maior que 0",       # DESCRIÇÃO DE COMO DEVE SER O ID
        gt=0,                                                       # MAIOR QUE 0
    ),
    db: any = Depends(fake_db)                                  # INJETANDO DEPENDENCIA DA FUNÇÃO fake_db
):  
    id = id - 1                                         # SUBTRAINDO 1 DO ID PARA QUE O ID SEJA IGUAL AO INDICE DA LISTA                         
    try:                                                # TENTA EXECUTAR O CÓDIGO
        return cursos[id]                               # RETORNA O CURSO COM O ID PASSADO
        return curso                                        # RETORNA O CURSO ESPECÍFICO PELO ID
    except:                                             # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                # LANÇA UMA EXCEÇÃO 
            status_code=status.HTTP_404_NOT_FOUND,          # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"      # DETALHES DA EXCEÇÃO - MENSAGEM
        )

@app.post("/cursos",                                        # ROTA PARA CRIAR UM CURSO
    summary="Criar um curso",                               # TITULO DA ROTA - APARECE NA DOCUMENTAÇÃO
    description="Criar um curso",                           # DESCRIÇÃO DA ROTA - APARECE NA DOCUMENTAÇÃO
    response_description="Curso criado",                    # DESCRIÇÃO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    response_model=Curso,                                   # MODELO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    status_code=status.HTTP_201_CREATED,                    # STATUS CODE DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    tags=["Cursos"]                                         # TAGS DA ROTA - APARECE NA DOCUMENTAÇÃO
    )   
async def post_curso(curso: Curso,                          # FUNÇÃO QUE CRIA UM CURSO
    db: any = Depends(fake_db)                              # INJETANDO DEPENDENCIA DA FUNÇÃO fake_db
):                         
    id = len(cursos) + 1                                    # ID DO CURSO
    cursos.append(curso)                                    # ADICIONA O CURSO NA LISTA DE CURSOS
    return curso                                            # RETORNA O CURSO CRIADO

@app.put("/cursos/{id}",
    summary="Atualizar um curso específico",                                # TITULO DA ROTA - APARECE NA DOCUMENTAÇÃO
    description="Atualizar um curso específico",                            # DESCRIÇÃO DA ROTA - APARECE NA DOCUMENTAÇÃO
    response_description="Curso atualizado",                                # DESCRIÇÃO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    response_model=Curso,                                                   # MODELO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    status_code=status.HTTP_200_OK,                                         # STATUS CODE DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    tags=["Cursos"]                                                         # TAGS DA ROTA - APARECE NA DOCUMENTAÇÃO
)              
async def put_curso(                                                        # FUNÇÃO QUE ATUALIZA UM CURSO
    id: int = Path (                                                        # ID DO CURSO - PATH PARAMETER
                    default=None,                                           # VALOR PADRÃO DO ID - CASO NÃO SEJA PASSADO NENHUM ID
                    title="O ID do curso",                                  # TÍTULO DO PARÂMETRO
                    description="Deve ser um numero inteiro maior que 0",   # DESCRIÇÃO DE COMO DEVE SER O ID
                    gt=0,                                                   # MAIOR QUE 0
                    example=1                                               # EXEMPLO DE COMO DEVE SER O ID           
                    ),

    curso: Curso = Body(                                                # CORPO DA REQUISIÇÃO - BODY PARAMETER
                    ...,                                
                       
        ),       

    db: any = Depends(fake_db)                                          # INJETANDO DEPENDENCIA DA FUNÇÃO fake_db
):                    
    try:                                                            # TENTA EXECUTAR O CÓDIGO
        curso = { **curso.dict(), "id": id }                        # FAZ A COPIA DO CURSO PASSADO E ADICIONA O ID VERDADEIRO
        cursos[id-1] = curso                                        # ATUALIZA O CURSO COM O ID PASSADO
        return curso                                                # RETORNA O CURSO ATUALIZADO
    except:                                                         # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                            # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                      # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"                  # DETALHES DA EXCEÇÃO - MENSAGEM
        )


@app.delete("/cursos/{id}",
    summary="Deletar um curso específico",                              # TITULO DA ROTA - APARECE NA DOCUMENTAÇÃO
    description="Deletar um curso específico",                          # DESCRIÇÃO DA ROTA - APARECE NA DOCUMENTAÇÃO
    response_description="Curso deletado",                              # DESCRIÇÃO DA RESPOSTA - APARECE NA DOCUMENTAÇÃO
    status_code=status.HTTP_204_NO_CONTENT,                             # STATUS CODE 204 NO CONTENT
    tags=["Cursos"]                                                     # TAGS DA ROTA - APARECE NA DOCUMENTAÇÃO
)                                                 
async def delete_curso(                                                     # FUNÇÃO QUE DELETA UM CURSO
    id: int = Path (                                                        # ID DO CURSO - PATH PARAMETER,
                    default=None,                                           # VALOR PADRÃO DO ID - CASO NÃO SEJA PASSADO NENHUM ID
                    title="O ID do curso",                                  # TÍTULO DO PARÂMETRO
                    description="Deve ser um numero inteiro maior que 0",   # DESCRIÇÃO DE COMO DEVE SER O ID
                    gt=0,                                                   # MAIOR QUE 0
                    example=1                                               # EXEMPLO DE COMO DEVE SER O ID
            ),                                                 
    db: any = Depends(fake_db)                                              # INJETANDO DEPENDENCIA DA FUNÇÃO fake_db
):  
    id = id - 1                                                             # SUBTRAINDO 1 DO ID PARA QUE O ID SEJA IGUAL AO INDICE DA LISTA                                          
    try:                                                                    # TENTA EXECUTAR O CÓDIGO
        del cursos[id]                                                          # DELETA O CURSO PELO ID
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)            # FORMA QUE DEVERIA SER FEITO - MAS NO FASTAPI ESTÁ BUGADO
        return Response(status_code=status.HTTP_204_NO_CONTENT)                 # RETORNA O STATUS CODE 204 NO CONTENT - PARA CASOS QUE NÃO POSSUEM RETORNO
    except:                                                                 # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                                    # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                              # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"                          # DETALHES DA EXCEÇÃO - MENSAGEM
        )

@app.get("/queryParams", status_code=status.HTTP_200_OK, tags=["Calculadora"])        # ROTA USANDO QUERY PARAMS - STATUS CODE 200 OK
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
