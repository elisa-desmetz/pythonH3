from flask import Flask, redirect, url_for, request
from flask import render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def redirection():
    return redirect(url_for('home'))
@app.route('/home/')
def home():
    return render_template("index.html")

@app.route('/projets/')
@app.route('/projets/projet-1/')
@app.route('/projets/projet-2/')
@app.route('/projets/projet-3/')
def abc():
    return render_template("projets.html")

@app.route('/contact/')
def aze():
    return render_template("main.html")

@app.route('/about/')
def zer():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5200")