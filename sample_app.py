# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_templates

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_templates("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
