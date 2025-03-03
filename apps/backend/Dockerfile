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

# Usar el entorno virtual de forma predeterminada
ENV PATH="/venv/bin:$PATH"

# Instalar dependencias en el entorno virtual
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r /app/requirements.txt

# Copiar todo el código del backend al contenedor
COPY apps/backend /app

# Exponer el puerto en el que Flask se ejecutará
EXPOSE 5000

# Establecer variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Comando para ejecutar el servidor Flask en desarrollo
CMD ["python", "app.py"]

# Comando para ejecutar el servidor Flask con Gunicorn
# CMD ["/venv/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]