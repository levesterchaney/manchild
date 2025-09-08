FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY manchild .
COPY manchild_server .
COPY manage.py .

EXPOSE 8000
