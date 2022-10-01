// INICIAR UM AMBIENTE VIRTUAL 

DIRETAMENTE NO POWERSHELL
	virtualenv nome-do-ambiente 

ATIVAR O AMBIENTE VIRTUAL
	.\nome-do-ambiente\Scripts\activate

###### CASO QUEIRA INSTALAR UM PROJETO 
	pip install -r requirements.txt

------------------------------------------------
	


DENTRO DO AMBIENTE VIRTUAL
	pip install fastapi uvicorn gunicorn
	
	CRIAR O ARQUIVO REQUIREMENTS
		pip freeze > requirements.txt
	INICIAR O SERVIDOR DA API
		uvicorn nomedoarquivoraiz:app
	INICIAR O SERVIDOR DA API COM AUTO RELOAD
		uvicorn nomedoarquivoraiz:app --reload

	CRIAR A CONDIÇÃO MAIN PARA EXECUTAR O ARQUIVO DIRETAMENTE
		python main.py

		**** PARA FAZER DEPLOY 
			pip install gunicorn
			pip freeze > requirements.txt
			gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

