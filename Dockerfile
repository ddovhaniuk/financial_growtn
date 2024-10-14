FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install prettytable


CMD ["python", "./main.py"]
