FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install pipenv

RUN pipenv install --system

ENTRYPOINT ["python3", "source/main.py"]




