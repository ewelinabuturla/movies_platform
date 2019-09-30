FROM python:3.6-slim
ENV PHYTONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv install --system

COPY . /app/
