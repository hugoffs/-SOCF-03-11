from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "<h1> Olá Mundo!! </h1>"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
