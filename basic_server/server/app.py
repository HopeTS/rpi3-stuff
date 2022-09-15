from flask import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Home page accessed")
    return "<p>hello world</p>"