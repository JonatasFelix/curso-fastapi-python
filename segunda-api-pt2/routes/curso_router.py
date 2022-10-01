from fastapi import APIRouter           # IMPORTANDO A CLASSE APIRouter - PARA CRIAR AS ROTAS 

router = APIRouter()                    # INSTANCIANDO A CLASSE APIRouter - PARA CRIAR AS ROTAS

@router.get("/api/vi/cursos")               #CRIANDO A ROTA PARA LISTAR OS CURSOS
async def get_cursos():                     # CRIANDO A FUNÇÃO PARA LISTAR OS CURSOS
    return {"cursos": "Lista de cursos"}    # RETORNANDO A LISTA DE CURSOS **