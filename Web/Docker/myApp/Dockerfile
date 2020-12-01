FROM python:3.8

WORKDIR /test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./app.py"]