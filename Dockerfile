# --- Etapa 1: Construcción y dependencias ---
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# --- Etapa 2: Imagen final ligera para producción ---
FROM python:3.11-alpine

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["python", "app.py"]
