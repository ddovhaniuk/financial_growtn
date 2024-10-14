FROM python:3-alpine3.4

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir math
RUN pip install --no-cache-dir matplotlib.pyplot
RUN pip install --no-cache-dir prettytable

CMD ["python", "./main.py"]
