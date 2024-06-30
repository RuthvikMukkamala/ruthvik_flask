from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/personal')
def personal_info():
    return render_template(...)

@app.route('/essays')
def essays():
    return render_template(...)

@app.route('/books')
def books():
    return render_template(...)


