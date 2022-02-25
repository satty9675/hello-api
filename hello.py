from flask import Flask
app = Flask(__name__)


@app.route("/ping")
def ping():
  return "ping success!!"

@app.route("/hello")
def hello_world():
  return "Hi from apivm01-us.east"
