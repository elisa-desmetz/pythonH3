FROM python:3.8

EXPOSE 8501

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENTRYPOINT ["streamlit", "run"]

CMD [ "app.py"]