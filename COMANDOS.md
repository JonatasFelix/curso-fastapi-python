// INICIAR UM AMBIENTE VIRTUAL 

DIRETAMENTE NO POWERSHELL
	virtualenv nome-do-ambiente 

ATIVAR O AMBIENTE VIRTUAL
	.\nome-do-ambiente\Scripts\activate

###### CASO QUEIRA INSTALAR UM PROJETO 
	pip install -r requirements.txt

------------------------------------------------



DENTRO DO AMBIENTE VIRTUAL
	pip install fastapi uvicorn
	
	CRIAR O ARQUIVO REQUIREMENTS
		pip freeze > requirements.txt
	INICIAR O SERVIDOR DA API
		uvicorn nomedoarquivoraiz:app
