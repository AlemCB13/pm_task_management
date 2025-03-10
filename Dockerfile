# Fase de construcción
FROM python:3.9-slim as builder
WORKDIR /app
RUN apt-get update && apt-get install -y gcc libpq-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip freeze > installed_packages.txt
COPY . .

# Fase final
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app /app
RUN cat /app/installed_packages.txt
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir fastapi uvicorn
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]