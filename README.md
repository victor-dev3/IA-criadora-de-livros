
# IA-criadora-de-livros

Projeto de criação de livros assistida por inteligência artificial, com código desenvolvido em Python.

## API Python com FastAPI e Llama 3.2

API desenvolvida em Python utilizando FastAPI e o modelo Llama 3.2, executado localmente pelo Ollama.

### Requisitos

- Python
- Ollama
- Modelo Llama 3.2
- Dependências listadas em `requirements.txt`

### Instalação

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Baixe o modelo:

```powershell
ollama pull llama3.2
```

### Execução

Inicie o Ollama e execute a API.

Se o arquivo principal for `main.py` e a instância FastAPI se chamar `app`, utilize:

```powershell
uvicorn main:app --reload
```

### Documentação da API

Com a API em execução, acesse:

http://127.0.0.1:8000/docs
