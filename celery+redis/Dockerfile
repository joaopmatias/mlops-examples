FROM python:3.8.10-slim-buster

RUN pip install celery[redis]

RUN mkdir /app
WORKDIR /app

COPY . .

CMD bash