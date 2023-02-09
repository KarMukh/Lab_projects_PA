from flask import Flask

app = Flask(__name__)


@app.route("/")
def les():
    return "<p>les!</p>"