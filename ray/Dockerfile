FROM python:3.8.10-slim-buster

RUN pip install ray[default]

RUN mkdir /app
WORKDIR /app

COPY . .

CMD bash