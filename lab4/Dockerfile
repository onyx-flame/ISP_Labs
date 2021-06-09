FROM python:3.9.5-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .