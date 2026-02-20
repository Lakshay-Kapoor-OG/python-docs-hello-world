from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello everyone, welcome to the world of Lakshay Kapoor"

if __name__ == "__main__":
    app.run()
