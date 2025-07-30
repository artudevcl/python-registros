# python base
FROM python:3.11-slim


# directorio de trabajo dentro del contenedor
WORKDIR /app

# copiar e instalar dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copiar todo el código del proyecto al contenedor
COPY . .

# puerto en el que correrá la API
EXPOSE 8000

# iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]