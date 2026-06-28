"""
API REST de um Fórum Online.

Disciplina: Cloud Computing - UNIDAVI
Tema individual: Sistema de Fórum Online

Expõe três rotas:
  GET /status         -> saúde da aplicação
  GET /topicos        -> lista de tópicos do fórum
  GET /topicos/{id}   -> um tópico específico pelo identificador

Os dados são carregados de um arquivo JSON externo (api/data/topicos.json),
e não embutidos como strings no código, conforme exigido no enunciado.
"""

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Forum API", version="1.0.0")

# Caminho do arquivo de dados, resolvido de forma relativa a este arquivo.
# Usar Path(__file__).parent evita que a API quebre dependendo do diretório
# a partir do qual o servidor é iniciado.
DATA_FILE = Path(__file__).parent / "data" / "topicos.json"


def carregar_topicos() -> list[dict]:
    """Lê e retorna a lista de tópicos do arquivo JSON externo."""
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


@app.get("/status")
def status():
    """Informações de saúde da aplicação."""
    return {
        "nome": "Forum API",
        "versao": app.version,
        "status": "online",
    }


@app.get("/topicos")
def listar_topicos():
    """Retorna todos os tópicos do fórum."""
    topicos = carregar_topicos()
    return {
        "total": len(topicos),
        "dados": topicos,
    }


@app.get("/topicos/{topico_id}")
def obter_topico(topico_id: int):
    """Retorna um único tópico pelo seu identificador.

    Responde 404 quando o identificador não existe na base.
    """
    topicos = carregar_topicos()
    for topico in topicos:
        if topico["id"] == topico_id:
            return {"dados": topico}
    raise HTTPException(
        status_code=404,
        detail=f"Tópico com id {topico_id} não encontrado.",
    )
