FROM python:3.10-slim-buster

WORKDIR /app

RUN pip3 install pipenv

COPY . .

RUN pipenv install

ENTRYPOINT ["python3", "source/main.py"]




