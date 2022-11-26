from flask import Flask
import re
app = Flask(__name__)
from datetime import datetime
from flask import render_template
app.static_folder = 'static'

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/EggBites")
def hello_there(name=None):
        return render_template(
        "EggBites2.html",
    )

@app.route("/ChickenCacciatore")
def hello_there(name=None):
        return render_template(
        "ChickenCacciatore2.html",
    )

@app.route("/CreamyChickenCasserole")
def hello_there(name=None):
        return render_template(
        "CreamyChickenCasserole2.html",
    )


@app.route("/About")
def hello_there(name=None):
        return render_template(
        "about.html",
    )


@app.route("/Contact")
def hello_there(name=None):
        return render_template(
        "contact.html"
    )

@app.route("/DevilsFoodCakeCookies")
def hello_there(name=None):
        return render_template(
        "DevilsFoodCakeCookies2.html"
    )

@app.route("/GuinnessBeefStew")
def hello_there(name=None):
        return render_template(
        "GuinnessBeefStew2.html"
    )

@app.route("/Index")
def hello_there(name=None):
        return render_template(
        "index.html"
    )

@app.route("/Index/<name>")
def hello_there(name=None):
        return render_template(
        "index.html",
        name=name,
        date=datetime.now()
    )

@app.route("/ProjectDetails")
def hello_there(name=None):
        return render_template(
        "project-details.html"
    )

@app.route("/Project")
def hello_there(name=None):
        return render_template(
        "project.html"
    )

@app.route("/RecipesSidebar")
def hello_there(name=None):
        return render_template(
        "recipes-sidebar.html"
    )

@app.route("/RecipesSidebar2")
def hello_there(name=None):
        return render_template(
        "recipes-sidebar2.html"
    )

@app.route("/UnstuffedCabbage")
def hello_there(name=None):
        return render_template(
        "UnstuffedCabbage2.html"
    )

@app.route("/ZucchiniBread")
def hello_there(name=None):
        return render_template(
        "ZucchiniBread2.html"
    )
