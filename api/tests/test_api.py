"""
Testes unitários da Forum API.

São quatro testes:
  1. (obrigatório) GET /topicos retorna HTTP 200;
  2. (obrigatório) estrutura do JSON contém os campos esperados;
  3. (obrigatório) GET /topicos/{id} inexistente retorna HTTP 404;
  4. (autoria própria) toda categoria pertence a um conjunto válido.

Usa o TestClient do FastAPI, que sobe a aplicação em memória — sem precisar
de um servidor real rodando, o que torna os testes rápidos e adequados ao CI.
"""

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)

# Conjunto fechado de categorias permitidas no fórum.
CATEGORIAS_VALIDAS = {
    "Programacao",
    "DevOps",
    "Hardware",
    "Carreira",
    "Geral",
    "Avisos",
}


def test_listar_topicos_retorna_200():
    """A rota de listagem deve responder com sucesso (HTTP 200)."""
    resposta = client.get("/topicos")
    assert resposta.status_code == 200


def test_estrutura_do_json_de_topicos():
    """Cada tópico deve conter os campos obrigatórios do domínio."""
    resposta = client.get("/topicos")
    corpo = resposta.json()

    assert "total" in corpo
    assert "dados" in corpo
    assert isinstance(corpo["dados"], list)
    assert len(corpo["dados"]) >= 10  # mínimo exigido no enunciado

    campos_esperados = {
        "id",
        "titulo",
        "autor",
        "categoria",
        "respostas",
        "visualizacoes",
        "fixado",
        "data_criacao",
    }
    for topico in corpo["dados"]:
        assert campos_esperados.issubset(topico.keys())


def test_topico_inexistente_retorna_404():
    """Buscar um id que não existe deve retornar HTTP 404."""
    resposta = client.get("/topicos/9999")
    assert resposta.status_code == 404
    assert "não encontrado" in resposta.json()["detail"]


def test_categorias_sao_validas():
    """Teste de autoria própria.

    Garante a integridade do domínio: nenhum tópico pode ter uma categoria
    fora do conjunto permitido. Em um fórum real, categorias livres geram
    inconsistência (ex.: 'Programação' vs 'programacao' vs 'Prog'), então
    validar contra um conjunto fechado previne dados sujos chegando à API.
    """
    resposta = client.get("/topicos")
    for topico in resposta.json()["dados"]:
        assert topico["categoria"] in CATEGORIAS_VALIDAS
