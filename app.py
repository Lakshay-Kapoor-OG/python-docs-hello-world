from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "fancy fancy fancy"
