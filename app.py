from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/personal')
def share_personal_info():
    ...


if __name__ == '__main__':
    app.run()
