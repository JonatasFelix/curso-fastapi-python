LIBS PARA INSTALAR - MYSQL

fastapi                 # Framework
sqlalchemy              # ORM
uvicorn                 # Servidor
mysql-connector-python  # Driver de mysql
asyncmy                 # Driver de mysql async
python-dotenv           # Ler variaveis de ambiente

pip install mysql-connector-python fastapi sqlalchemy uvicorn aiomysql
pip freeze > requirements.txt
