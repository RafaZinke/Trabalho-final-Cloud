# Imagem base enxuta com Python 3.12.
FROM python:3.12-slim

# Diretório de trabalho dentro do container.
WORKDIR /app

# Instala as dependências primeiro, aproveitando o cache de camadas do Docker:
# se o requirements.txt não mudar, esta camada não é reconstruída.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação.
COPY api/ ./api/

# Porta exposta pela aplicação.
EXPOSE 8000

# Sobe o servidor acessível externamente ao container (0.0.0.0).
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
