import aiml
from flask import Flask
from flask import render_template
import os


kernel = aiml.Kernel()

for filename in os.listdir("brain"):
	if filename.endswith(".aiml"):
		kernel.learn("brain/" + filename)

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/<query>")
def api(query):
	return kernel.respond(query)


if __name__ == "__main__":
	app.run(debug=True)