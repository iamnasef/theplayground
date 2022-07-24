from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World"

app.run(port=1234, debug=True)