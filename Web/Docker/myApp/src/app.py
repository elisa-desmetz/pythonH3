# app.py - a minimal flask api using flask_restful
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<title>Hello H3!</title><h1>Hello !</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')