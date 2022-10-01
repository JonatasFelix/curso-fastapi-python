from typing import Optional     # PRECISA IMPORTAR A OPÇÃO DE OPCIONAL - USADA NO ID
from pydantic import BaseModel  # BASE MODEL É UMA CLASSE QUE SERÁ USADA PARA VALIDAR OS DADOS DE ENTRADA

class Curso(BaseModel):  # CLASSE QUE REPRESENTA UM CURSO EXTENDENDO A CLASSE BaseModel
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo='Python', aulas=10, horas=20),
    Curso(id=2, titulo='Django', aulas=10, horas=20),
    Curso(id=3, titulo='Flask', aulas=10, horas=20),
    Curso(id=4, titulo='FastAPI', aulas=10, horas=20),
    Curso(id=5, titulo='Docker', aulas=10, horas=20)
]