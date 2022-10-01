from typing import Optional     # PRECISA IMPORTAR A OPÇÃO DE OPCIONAL - USADA NO ID
from pydantic import BaseModel  # BASE MODEL É UMA CLASSE QUE SERÁ USADA PARA VALIDAR OS DADOS DE ENTRADA
from pydantic import validator  # VALIDATOR É UMA FUNÇÃO QUE SERÁ USADA PARA VALIDAR OS DADOS DE ENTRADA

class Curso(BaseModel):  # CLASSE QUE REPRESENTA UM CURSO EXTENDENDO A CLASSE BaseModel
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')  # VALIDATOR PARA O TÍTULO
    def titulo_maior_que_1_palavra(cls, value):                           # FUNÇÃO QUE VALIDA SE O TÍTULO TEM MAIS DE UMA PALAVRA
        if len(value.replace(" ", "")) < 5:                               # SE O TÍTULO TIVER MENOS DE 5 CARACTERES
            raise ValueError('O titulo precisa ter mais de 4 caracteres') # RETORNA UMA MENSAGEM DE ERRO
        
        titulo = value.strip().split(" ")                                 # TRANSFORMA O TÍTULO EM UMA LISTA DE PALAVRAS E REMOVE OS ESPAÇOS EM BRANCO
        if len(titulo) < 2:                                               # SE O TÍTULO TIVER MENOS DE 2 PALAVRAS
            raise ValueError('O titulo precisa ter mais de uma palavra')  # RETORNA UMA MENSAGEM DE ERRO

        return value.strip().title()                                      # RETORNA O TÍTULO SEM ESPAÇOS EM BRANCO E COM A PRIMEIRA LETRA MAIÚSCULA

    @validator('aulas')  # VALIDATOR PARA AS AULAS
    def aulas_maior_que_0(cls, value):  # FUNÇÃO QUE VALIDA SE O NÚMERO DE AULAS É MAIOR QUE 0
        if value < 1:                  # SE O NÚMERO DE AULAS FOR MENOR QUE 1
            raise ValueError('O número de aulas precisa ser maior que 0')  # RETORNA UMA MENSAGEM DE ERRO
        
        if type(value) != int:         # SE O NÚMERO DE AULAS NÃO FOR UM INTEIRO
            raise ValueError('O número de aulas precisa ser um número inteiro')  # RETORNA UMA MENSAGEM DE ERRO
        
        return value                   # RETORNA O NÚMERO DE AULAS

    @validator('horas')  # VALIDATOR PARA AS HORAS
    def horas_maior_que_0(cls, value):  # FUNÇÃO QUE VALIDA SE O NÚMERO DE HORAS É MAIOR QUE 0
        if value < 1:                  # SE O NÚMERO DE HORAS FOR MENOR QUE 1
            raise ValueError('O número de horas precisa ser maior que 0')  # RETORNA UMA MENSAGEM DE ERRO

        if type(value) != int:         # SE O NÚMERO DE HORAS NÃO FOR UM INTEIRO
            raise ValueError('O número de horas precisa ser um número inteiro')  # RETORNA UMA MENSAGEM DE ERRO

        return value                   # RETORNA O NÚMERO DE HORAS


cursos = [
    Curso(id=1, titulo='Curso de Python', aulas=10, horas=20),
    Curso(id=2, titulo='Curso de Django', aulas=10, horas=20),
    Curso(id=3, titulo='Curso de Flask', aulas=10, horas=20),
    Curso(id=4, titulo='Curso de FastAPI', aulas=10, horas=20),
    Curso(id=5, titulo='Curso de Docker', aulas=10, horas=20)
]

