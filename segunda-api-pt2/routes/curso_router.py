from fastapi import APIRouter           # IMPORTANDO A CLASSE APIRouter - PARA CRIAR AS ROTAS 
from typing import List                 # IMPORTANDO A CLASSE List - PARA CRIAR A LISTA DE CURSOS
from fastapi import status              # IMPORTANDO A CLASSE status - PARA CRIAR O STATUS HTTP
from fastapi import Path                # IMPORTANDO A CLASSE Path - PARA CRIAR O CAMINHO DA ROTA
from fastapi import HTTPException       # IMPORTANDO A CLASSE HTTPException - PARA CRIAR A EXCEÇÃO HTTP
from fastapi import Body                # IMPORTANDO A CLASSE Body - PARA CRIAR O CORPO DA ROTA
from fastapi import Response            # IMPORTANDO A CLASSE Response - PARA CRIAR A RESPOSTA DA ROTA

from models import Curso, cursos

router = APIRouter()                    # INSTANCIANDO A CLASSE APIRouter - PARA CRIAR AS ROTAS

@router.get("/api/vi/cursos",               # CRIANDO A ROTA PARA LISTAR OS CURSOS
            response_model=list[Curso],     # DEFININDO O TIPO DE RETORNO DA ROTA
            status_code=status.HTTP_200_OK # DEFININDO O STATUS HTTP DA ROTA
)               
async def get_cursos():                     # CRIANDO A FUNÇÃO PARA LISTAR OS CURSOS
    return cursos                           # RETORNANDO A LISTA DE CURSOS

@router.get("/api/vi/cursos/{curso_id}",    # CRIANDO A ROTA PARA LISTAR OS CURSOS
            response_model=Curso,           # DEFININDO O TIPO DE RETORNO DA ROTA
            status_code=status.HTTP_200_OK  # DEFININDO O STATUS HTTP DA ROTA
)

async def get_curso(curso_id: int = Path(
    default=None,                                   # DEFININDO O VALOR PADRÃO DO PARÂMETRO
    title="ID do curso",                            # TÍTULO DO PARÂMETRO
    description="ID do curso que será buscado",     # DEFININDO A DESCRIÇÃO DA ROTA
    gt=0,                                           # O ID DO CURSO DEVE SER MAIOR QUE 0
    le=len(cursos)                                  # O VALOR MAXIMO DE curso_id É O TAMANHO DA LISTA DE CURSOS
    )
):
    try:                                                        # TENTANDO EXECUTAR O CÓDIGO
        curso = cursos[curso_id - 1]                            # BUSCANDO O CURSO PELO ID
        return curso                                                # RETORNANDO O CURSO CASO ELE EXISTA                               
    except:                                                     # CASO NÃO EXISTA O CURSO
        raise HTTPException(                                        # LANÇANDO A EXCEÇÃO HTTP
            status_code=status.HTTP_404_NOT_FOUND,                      # RETORNANDO O STATUS HTTP 404
            detail=f"Curso com id {curso_id} não encontrado"            # RETORNANDO A MENSAGEM DE ERRO
        )


@router.post("/api/vi/cursos",                                      # CRIANDO A ROTA PARA CRIAR UM CURSO
            summary="Cria um curso",                                # DEFININDO O RESUMO DA ROTA
            description="Cria um curso no banco de dados",          # DEFININDO A DESCRIÇÃO DA ROTA
            response_model=Curso,                                   # DEFININDO O TIPO DE RETORNO DA ROTA
            status_code=status.HTTP_201_CREATED                     # RETORNANDO O STATUS HTTP 201
)
async def post_curso(curso: Curso):                         
    id = len(cursos) + 1                                    # ID DO CURSO
    curso.id = id                                           # SETANDO O ID DO CURSO
    cursos.append(curso)                                    # ADICIONA O CURSO NA LISTA DE CURSOS
    return curso 



@router.put("/api/vi/cursos/{curso_id}",                                # CRIANDO A ROTA PARA ATUALIZAR UM CURSO
            summary="Atualiza um curso",                                # DEFININDO O RESUMO DA ROTA
            description="Atualiza um curso no banco de dados",          # DEFININDO A DESCRIÇÃO DA ROTA
            response_model=Curso,                                       # DEFININDO O TIPO DE RETORNO DA ROTA
            status_code=status.HTTP_200_OK                              # RETORNANDO O STATUS HTTP 200
)
async def put_curso(                                                        # FUNÇÃO QUE ATUALIZA UM CURSO
    curso_id: int = Path (                                                        # ID DO CURSO - PATH PARAMETER
                    default=None,                                           # VALOR PADRÃO DO ID - CASO NÃO SEJA PASSADO NENHUM ID
                    title="O ID do curso",                                  # TÍTULO DO PARÂMETRO
                    description="Deve ser um numero inteiro maior que 0",   # DESCRIÇÃO DE COMO DEVE SER O ID
                    gt=0,                                                   # MAIOR QUE 0
                    example=1                                               # EXEMPLO DE COMO DEVE SER O ID           
                    ),

    curso: Curso = Body(                                                # CORPO DA REQUISIÇÃO - BODY PARAMETER
                    ...,                                              
        )
):                    
    try:                                                            # TENTA EXECUTAR O CÓDIGO
        curso.id = curso_id                                         # SETA O ID DO CURSO
        cursos[curso_id-1] = curso                                        # ATUALIZA O CURSO COM O ID PASSADO
        return curso                                                # RETORNA O CURSO ATUALIZADO
    except:                                                         # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                            # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                      # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"                  # DETALHES DA EXCEÇÃO - MENSAGEM
        )


@router.delete("/api/vi/cursos/{curso_id}",                           # CRIANDO A ROTA PARA DELETAR UM CURSO
            status_code=status.HTTP_204_NO_CONTENT                     # RETORNANDO O STATUS HTTP 204
)
async def delete_curso(                                                     # FUNÇÃO QUE DELETA UM CURSO
    curso_id: int = Path (                                                        # ID DO CURSO - PATH PARAMETER
                    default=None,                                           # VALOR PADRÃO DO ID - CASO NÃO SEJA PASSADO NENHUM ID
                    title="O ID do curso",                                  # TÍTULO DO PARÂMETRO
                    description="Deve ser um numero inteiro maior que 0",   # DESCRIÇÃO DE COMO DEVE SER O ID
                    gt=0,                                                   # MAIOR QUE 0
                    example=1                                               # EXEMPLO DE COMO DEVE SER O ID
                    )
):
    try:                                                            # TENTA EXECUTAR O CÓDIGO
        cursos.pop(curso_id-1)                                      # REMOVE O CURSO DA LISTA DE CURSOS
        return Response(status_code=status.HTTP_204_NO_CONTENT)      # RETORNA O STATUS HTTP 204
    except:                                                         # CASO NÃO ENCONTRE O ID DO CURSO
        raise HTTPException(                                            # LANÇA UMA EXCEÇÃO
            status_code=status.HTTP_404_NOT_FOUND,                      # STATUS CODE 404  NOT FOUND
            detail=f"Curso com id {id} não encontrado"                  # DETALHES DA EXCEÇÃO - MENSAGEM
        )