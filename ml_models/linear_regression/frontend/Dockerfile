FROM python:3.10-slim

WORKDIR /frontend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Entrena y genera el artefacto en el build
RUN python train.py

EXPOSE 8001

CMD gunicorn config.wsgi:application --bind 0.0.0:$[PORT:-8001]