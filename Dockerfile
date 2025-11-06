# ===========================
# Dockerfile - Fan-Worker-Sink
# ===========================

# 1️⃣ Imagen base
FROM python:3.11-slim

# 2️⃣ Configurar directorio de trabajo
WORKDIR /app

# 3️⃣ Instalar dependencias del sistema y Python en una sola capa
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    python -m pip install --upgrade pip && \
    pip install pytest pytest-cov

# 4️⃣ Copiar archivos necesarios
COPY requirements.txt .
COPY src/ ./src
COPY tests/ ./tests
COPY pytest.ini .

# 5️⃣ Instalar dependencias de Python
RUN pip install -r requirements.txt

# 6️⃣ Variables de entorno
# Modo de ejecución: run para pipeline, test para pruebas
ENV MODE=run

# 7️⃣ Comando por defecto
CMD if [ "$MODE" = "test" ]; then \
    pytest --cov=src --cov-report=term-missing --cov-report=html tests; \
    else \
    python src/run.py; \
    fi
