from fastapi import APIRouter
from api.v1.endpoints import cursos

v1_router = APIRouter()

v1_router.include_router(cursos.router, prefix="/cursos", tags=["cursos"])

# /api/v1/cursos -- GET ROTA ADICIONADA NO CORE\CONFIG.PY