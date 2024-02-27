from  flask import Flask

app = Flask(__name__)

@app.route("/")
def warm_up():
  return "<p>Hello, xesquedele World!</p>"