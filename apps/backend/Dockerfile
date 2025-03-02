# Usar la versión más reciente de Python (3.13-alpine)
FROM python:3.13-alpine

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev

# Copiar SOLO requirements.txt antes del código para aprovechar caché de Docker
COPY apps/backend/requirements.txt /app/requirements.txt

# Crear un entorno virtual en /venv
RUN python -m venv /venv

# Instalar dependencias en el entorno virtual
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt

# Ahora copiar TODO el código después de instalar dependencias
COPY apps/backend /app

# Verificar si `app.py` existe
RUN ls -la /app

# Exponer el puerto en el que Flask se ejecutará
EXPOSE 5000

# Comando para ejecutar el servidor Flask
CMD ["/venv/bin/python", "/app/app.py"]
