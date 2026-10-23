
# API Python com FastAPI e Llama 3.2

Projeto de API desenvolvido em Python utilizando FastAPI
e o modelo Llama 3.2 executado localmente pelo Ollama.

## Requisitos
- Python
- Ollama
- Modelo Llama 3.2

## Instalação

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
ollama pull llama3.2
```

## Execução

Inicie o Ollama e execute a API conforme o arquivo
principal do projeto.

Exemplo, se o arquivo principal for main.py:

```powershell
uvicorn main:app --reload
```

## Documentação da API

Depois de iniciar a aplicação, acesse:

http://127.0.0.1:8000/docs
