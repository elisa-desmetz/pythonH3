FROM python:3.8-alpine

EXPOSE 5200

WORKDIR /test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./app.py"]