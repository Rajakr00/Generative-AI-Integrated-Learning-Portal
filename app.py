from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Team 12!</p>"


if __name__ == "__main__":
    app.run()
