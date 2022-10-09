from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ["GET, POST"])
def index():
    return "its being built, don't worry!!"


app.run(debug=True, port=8000, host="0.0.0.0")