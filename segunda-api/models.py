from typing import Optional     # PRECISA IMPORTAR A OPÇÃO DE OPCIONAL - USADA NO ID
from pydantic import BaseModel  # BASE MODEL É UMA CLASSE QUE SERÁ USADA PARA VALIDAR OS DADOS DE ENTRADA

class Curso(BaseModel):  # CLASSE QUE REPRESENTA UM CURSO EXTENDENDO A CLASSE BaseModel
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int