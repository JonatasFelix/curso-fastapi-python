from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schemas import CursoSchema
from core.deps import get_session

from api.v1.error.base_error import BaseError

router = APIRouter()

# POST CURSO
@router.post("/",                           # ROTA PARA CRIAR UM CURSO
    response_model=CursoSchema,             # RETORNA O CURSO CRIADO
    status_code=status.HTTP_201_CREATED     # STATUS CODE PARA RETORNO
)
async def criar_curso(  curso: CursoSchema,                             #RECEBE O CORPO DO CURSO
                        db: AsyncSession = Depends(get_session)    #RECEBE A SESSÃO DO BANCO DE DADOS - DEPENDÊNCIA DO GET_SESSION - INJEÇÃO DE DEPENDENCIA
                    ):
    novo_curso = CursoModel(    # CRIA UM NOVO CURSO
        titulo=curso.titulo,    # TÍTULO DO CURSO
        aulas=curso.aulas,      # QUANTIDADE DE AULAS
        horas=curso.horas       # QUANTIDADE DE HORAS
    )
    db.add(novo_curso)  # ADICIONA O CURSO NO BANCO DE DADOS
    await db.commit()   # SALVA AS ALTERAÇÕES NO BANCO DE DADOS

    return novo_curso   # RETORNA O CURSO CRIADO



# GET ALL
@router.get("/",                            # ROTA PARA LISTAR TODOS OS CURSOS
    summary="Lista todos os cursos",        # SUMÁRIO DA ROTA
    description="Lista todos os cursos",    # DESCRIÇÃO DA ROTA
    response_description="Lista de cursos", # DESCRIÇÃO DA RESPOSTA
    status_code=status.HTTP_200_OK,         # STATUS CODE PARA RETORNO
    response_model=List[CursoSchema]        # RETORNA UMA LISTA DE CURSOS - LISTA DE CURSO SCHEMA
    )
async def listar_cursos(                        # FUNÇÃO QUE VAI LISTAR TODOS OS CURSOS
    db: AsyncSession = Depends(get_session)     # RECEBE A SESSÃO DO BANCO DE DADOS - DEPENDÊNCIA DO GET_SESSION - INJEÇÃO DE DEPENDENCIA
):
    async with db as session:
        query = select(CursoModel)                                  # SELECIONA TODOS OS CURSOS DA TABELA
        result = await session.execute(query)                       # EXECUTA A QUERY - QUERY É UMA FUNÇÃO DO SQLALCHEMY
        cursos: List[CursoModel] = result.scalars().all()           # RETORNA TODOS OS CURSOS - SCALARS() É PARA RETORNAR UMA LISTA DE CURSOS - ALL() É PARA RETORNAR TODOS OS CURSOS

        if not cursos:                                              # SE NÃO TIVER CURSOS
            raise BaseError(                                        # LANÇA UM ERRO
                status_code=status.HTTP_404_NOT_FOUND,              # STATUS CODE PARA RETORNO
                message="Nenhum curso encontrado"                   # MENSAGEM DE ERRO
            )
        
        return cursos                                               # RETORNA A LISTA DE CURSOS


# GET BY ID
@router.get("/{curso_id}",                        # ROTA PARA LISTAR UM CURSO PELO ID
    response_model=CursoSchema,                   # RETORNA UM CURSO
    status_code=status.HTTP_200_OK                # STATUS CODE PARA RETORNO
    )
async def listar_curso_por_id(                                              # FUNÇÃO QUE VAI LISTAR UM CURSO PELO ID
                                curso_id: int,                              # RECEBE O ID DO CURSO
                                db: AsyncSession = Depends(get_session)     # RECEBE A SESSÃO DO BANCO DE DADOS - DEPENDÊNCIA DO GET_SESSION - INJEÇÃO DE DEPENDENCIA
                            ):
    # ASYNC WITH É UMA FORMA DE FAZER O TRY CATCH DO PYTHON                        
    async with db as session:

        # PEGA O CURSO PELO ID - SQLALCHEMY
        query = select(CursoModel).where(CursoModel.id == curso_id)     # SELECIONA O CURSO PELO ID - SQLALCHEMY
        result = await session.execute(query)                           # EXECUTA A QUERY - QUERY É UMA FUNÇÃO DO SQLALCHEMY
        curso: CursoModel = result.scalar_one_or_none()                 # RETORNA O CURSO - SCALAR_ONE_OR_NONE() É PARA RETORNAR UM CURSO - ONE() É PARA RETORNAR APENAS UM CURSO
        
        # SE O CURSO NÃO EXISTIR - LANÇA UMA EXCEÇÃO 404 NOT FOUND
        if not curso:                                                   # SE NÃO EXISTIR CURSO
            raise BaseError(                                        # LANÇA UM ERRO
                status_code=status.HTTP_404_NOT_FOUND,              # STATUS CODE PARA RETORNO
                message="Nenhum curso encontrado"                   # MENSAGEM DE ERRO
            )
        
        return curso                                                    # RETORNA O CURSO - SE EXISTIR
    

# PUT CURSO
@router.put("/{curso_id}",                          # ROTA PARA ATUALIZAR UM CURSO
    response_model=CursoSchema,                     # RETORNA O CURSO ATUALIZADO
    status_code=status.HTTP_200_OK                  # STATUS CODE PARA RETORNO
    )
async def atualizar_curso(                                          # FUNÇÃO QUE VAI ATUALIZAR UM CURSO
                            curso_id: int,                          # RECEBE O ID DO CURSO
                            curso: CursoSchema,                     # RECEBE O CORPO DO CURSO
                            db: AsyncSession = Depends(get_session) # RECEBE A SESSÃO DO BANCO DE DADOS - DEPENDÊNCIA DO GET_SESSION - INJEÇÃO DE DEPENDENCIA
                        ):
    async with db as session:

        # BUSCA O CURSO PELO ID - SQLALCHEMY
        query = select(CursoModel).where(CursoModel.id == curso_id)     # SELECIONA O CURSO PELO ID - SQLALCHEMY
        result = await session.execute(query)                           # EXECUTA A QUERY - QUERY É UMA FUNÇÃO DO SQLALCHEMY
        curso_bd: CursoModel = result.scalar_one_or_none()              # RETORNA O CURSO - SCALAR_ONE_OR_NONE() É PARA RETORNAR UM CURSO - ONE() É PARA RETORNAR APENAS UM CURSO
        
        # SE NÃO EXISTIR CURSO - LANÇA UMA EXCEÇÃO 404 NOT FOUND - FUNÇÃO DO FASTAPI
        if not curso_bd:                                                                # SE NÃO EXISTIR CURSO
            raise BaseError(                                        # LANÇA UM ERRO
                status_code=status.HTTP_404_NOT_FOUND,              # STATUS CODE PARA RETORNO
                message="Nenhum curso encontrado"                   # MENSAGEM DE ERRO
            )

        # CASO O CURSO EXISTA, ATUALIZA OS DADOS - SQLALCHEMY
        curso_bd.titulo = curso.titulo                                   # ATUALIZA O TÍTULO DO CURSO
        curso_bd.aulas = curso.aulas                                     # ATUALIZA A QUANTIDADE DE AULAS DO CURSO
        curso_bd.horas = curso.horas                                     # ATUALIZA A QUANTIDADE DE HORAS DO CURSO
        await session.commit()                                           # SALVA AS ALTERAÇÕES NO BANCO DE DADOS
        return curso_bd                                                  # RETORNA O CURSO ATUALIZADO



# DELETE CURSO
@router.delete("/{curso_id}",                           # ROTA PARA DELETAR UM CURSO
    status_code=status.HTTP_204_NO_CONTENT              # STATUS CODE PARA RETORNO
    )
async def deletar_curso(                                                # FUNÇÃO QUE VAI DELETAR UM CURSO
                            curso_id: int,                              # RECEBE O ID DO CURSO
                            db: AsyncSession = Depends(get_session)     # RECEBE A SESSÃO DO BANCO DE DADOS - DEPENDÊNCIA DO GET_SESSION - INJEÇÃO DE DEPENDENCIA
                        ):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)     # SELECIONA O CURSO PELO ID - SQLALCHEMY
        result = await session.execute(query)                           # EXECUTA A QUERY - QUERY É UMA FUNÇÃO DO SQLALCHEMY
        curso_bd: CursoModel = result.scalar_one_or_none()              # RETORNA O CURSO - SCALAR_ONE_OR_NONE() É PARA RETORNAR UM CURSO - ONE() É PARA RETORNAR APENAS UM CURSO

        # SE NÃO EXISTIR CURSO - LANÇA UMA EXCEÇÃO 404 NOT FOUND - FUNÇÃO DO FASTAPI
        if not curso_bd:                                                                # SE NÃO EXISTIR CURSO
            raise BaseError(                                        # LANÇA UM ERRO
                status_code=status.HTTP_404_NOT_FOUND,              # STATUS CODE PARA RETORNO
                message="Nenhum curso encontrado"                   # MENSAGEM DE ERRO
            )

        # CASO O CURSO EXISTA, DELETA O CURSO - SQLALCHEMY
        await session.delete(curso_bd)                                  # DELETA O CURSO
        await session.commit()                                          # SALVA AS ALTERAÇÕES NO BANCO DE DADOS

        return Response(status_code=status.HTTP_204_NO_CONTENT)         # RETORNA O STATUS CODE 204 NO CONTENT
