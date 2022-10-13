from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET, POST"])
@app.route("/<name>")
def index(name="Recipe Book"):
    # not needed thanks to @app.route(/<name>):
    #       name = request.args.get("name", name)
    return "Hello from {}".format(name)


app.run(debug=True, port=8000, host="0.0.0.0")