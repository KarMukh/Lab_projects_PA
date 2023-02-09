from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/")
def hi():
    return "<p>Hi!</p>"

@app.route("/")
def ho():
    return "<p>Hol!</p>"
