from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/personal')
def personal_info():
    return render_template("personal.html")

@app.route('/research')
def research_info():
    return render_template("research.html")

@app.route('/projects')
def project_info():
    return render_template("projects.html")





