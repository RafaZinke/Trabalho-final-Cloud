# Forum API

API REST de um **Fórum Online**, desenvolvida para o Trabalho Final da disciplina de
Cloud Computing (UNIDAVI). Construída com **Python + FastAPI**, com testes unitários
em `pytest` e pipeline de Integração Contínua no GitHub Actions.

## Estrutura do projeto

```
forum-api/
├── api/
│   ├── app.py              # Código-fonte da API
│   ├── data/
│   │   └── topicos.json    # Dados simulados (12 tópicos)
│   └── tests/
│       └── test_api.py     # Testes unitários
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de CI
├── requirements.txt
└── README.md
```

## Rotas

| Método | Rota              | Descrição                                  |
|--------|-------------------|--------------------------------------------|
| GET    | `/status`         | Saúde da aplicação (nome, versão, status)  |
| GET    | `/topicos`        | Lista todos os tópicos do fórum            |
| GET    | `/topicos/{id}`   | Retorna um tópico pelo identificador       |

Códigos HTTP: `200` (sucesso), `404` (tópico inexistente).

## Pré-requisitos

- Python 3.12+
- (Opcional) Docker, para execução em container

## Execução local (sem container)

```bash
# 1. Criar e ativar um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Subir a API (a partir da raiz do projeto)
uvicorn api.app:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.
Documentação interativa (Swagger) em `http://127.0.0.1:8000/docs`.

## Execução com container (Docker)

```bash
# Construir a imagem
docker build -t forum-api .

# Rodar o container
docker run -p 8000:8000 forum-api
```

## Rodando os testes

```bash
python -m pytest -v
```

## Lint

```bash
ruff check api/
```
