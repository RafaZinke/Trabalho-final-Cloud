Forum API

API REST de um Fórum Online, desenvolvida para o Trabalho Final da disciplina de
Cloud Computing (UNIDAVI). Construída com Python + FastAPI, com testes unitários
em pytest, análise estática com ruff e pipeline de Integração Contínua no GitHub Actions.


Autor: Rafael Zink
Tema individual: Sistema de Fórum Online
Repositório: https://github.com/RafaZinke/Trabalho-final-Cloud


Estrutura do projeto

Trabalho-final-Cloud/
├── api/
│   ├── app.py              # Código-fonte da API
│   ├── __init__.py
│   ├── data/
│   │   └── topicos.json    # Dados simulados (12 tópicos)
│   └── tests/
│       └── test_api.py     # Testes unitários
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de CI
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

Rotas

MétodoRotaDescriçãoGET/statusSaúde da aplicação (nome, versão, status)GET/topicosLista todos os tópicos do fórum + totalGET/topicos/{id}Retorna um único tópico pelo identificador

Códigos HTTP retornados: 200 (sucesso) e 404 (tópico inexistente).
Documentação interativa (Swagger) disponível em /docs.

Pré-requisitos


Python 3.12+
(Opcional) Docker, para execução em container


Execução local (sem container)

bash# 1. Criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\activate           # Windows (PowerShell)
# source .venv/bin/activate      # Linux/macOS

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Subir a API (a partir da raiz do projeto)
python -m uvicorn api.app:app --reload

A API ficará disponível em http://127.0.0.1:8000.
Acesse http://127.0.0.1:8000/docs para a documentação interativa (Swagger).


Observação (Windows): caso os comandos uvicorn, pytest ou ruff não sejam
reconhecidos diretamente no PowerShell (por não estarem no PATH), execute-os por meio
do interpretador, na forma python -m <ferramenta>, conforme mostrado acima.



Execução com container (Docker)

bash# Construir a imagem
docker build -t forum-api .

# Rodar o container
docker run -p 8000:8000 forum-api

A API ficará acessível em http://127.0.0.1:8000.

Rodando os testes

bashpython -m pytest -v

Análise estática (lint)

bashpython -m ruff check api/

Integração Contínua

A cada push ou pull request, o GitHub Actions executa automaticamente o pipeline
definido em .github/workflows/ci.yml, que realiza o checkout do código, configura o
ambiente Python, instala as dependências, roda o ruff (lint) e executa os testes com
pytest. Se qualquer etapa falhar, o pipeline é marcado como malsucedido.