from fastapi import APIRouter       # IMPORTANDO A CLASSE APIRouter - PARA CRIAR AS ROTAS 

router = APIRouter()                # INSTANCIANDO A CLASSE APIRouter - PARA CRIAR AS ROTAS

@router.get("/api/vi/usuarios")                 #CRIANDO A ROTA PARA LISTAR OS USUARIOS
async def get_usuarios():                       # CRIANDO A FUNÇÃO PARA LISTAR OS USUARIOS
    return {"usuarios": "Lista de usuarios"}    # RETORNANDO A LISTA DE USUARIOS **