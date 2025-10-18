#imagen
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

COPY . .
# install dependencies
RUN pip install flask

#comando para ejecutar
CMD ["python", "main_server.py"]