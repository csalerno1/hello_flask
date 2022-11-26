from flask import Flask
import re
app = Flask(__name__)
from datetime import datetime
from flask import render_template
app.static_folder = 'static'

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hi")
def hello_there(name=None):
        return render_template(
        "EggBites2.html",
        name=name,
        date=datetime.now()
    )