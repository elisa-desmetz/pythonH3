from flask import Flask
from flask import render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<title>Hello H3!</title><h1>Hello !</h1>'

@app.route('/hello/')
def hello():
    return 'Hello !'

@app.route('/hello/<string:username>')
def show_user(username):
    return 'Hello %s !' % escape(username)

@app.route('/hello_template/<string:username>')
def show_user_profile(username=None):
    return render_template("hello_you.html", username=username)