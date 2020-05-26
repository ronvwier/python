from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/name/<name>")
def user(name):
    return f'Hello {name}!'

#if __name__ == "__main__":

app.run()
