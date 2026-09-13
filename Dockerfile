# Estágio base utilizando imagem oficial enxuta do Python 3.12
FROM python:3.12-slim

# Instala o utilitário uv para gerenciamento rápido de pacotes
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Configura variáveis de ambiente para otimizar o Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_SYSTEM_PYTHON=1

# Copia os arquivos de configuração e todo o código-fonte/artefatos necessários
COPY pyproject.toml README.md ./
COPY src/ ./src/
COPY models/ ./models/

# Instala as dependências do projeto e o pacote local utilizando o uv
RUN uv pip install --no-cache -e .

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando padrão para iniciar a aplicação via Uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]