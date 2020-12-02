from flask import Flask, redirect, url_for
from flask import render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def redirection():
    return redirect(url_for('home'))
@app.route('/home/')
def home():
    return render_template("index.html")

@app.route('/project/')
def abc():
    return '<title>Hello H3!</title><h1>Hello !</h1>'

@app.route('/contact/')
def aze():
    return '<title>Hello H3!</title><h1>Hello !</h1>'

@app.route('/about/')
def zer():
    return '<title>About</title><h1>Powered by Heroku</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')