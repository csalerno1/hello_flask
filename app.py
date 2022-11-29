from flask import Flask
import re
app = Flask(__name__)
from flask import render_template
app.static_folder = 'static'


@app.route("/EggBites")
def EggBites():
        return render_template(
        "EggBites2.html",
    )

@app.route("/ChickenCacciatore")
def ChickenCacciatore():
        return render_template(
        "ChickenCacciatore2.html",
    )

@app.route("/CreamyChickenCasserole")
def CreamyChickenCasserole():
        return render_template(
        "CreamyChickenCasserole2.html",
    )


@app.route("/About")
def About():
        return render_template(
        "about.html",
    )


@app.route("/Contact")
def Contact():
        return render_template(
        "contact.html"
    )

@app.route("/DevilsFoodCakeCookies")
def DevilsFoodCakeCookies():
        return render_template(
        "DevilsFoodCakeCookies2.html"
    )

@app.route("/GuinnessBeefStew")
def GuinnessBeefStew():
        return render_template(
        "GuinnessBeefStew2.html"
    )

@app.route("/")
def Index():
        return render_template(
        "index.html"
    )

@app.route("/ProjectDetails")
def ProjectDetails():
        return render_template(
        "project-details.html"
    )

@app.route("/Project")
def Project():
        return render_template(
        "project.html"
    )

@app.route("/RecipesSidebar")
def RecipesSidebar():
        return render_template(
        "recipes-sidebar.html"
    )

@app.route("/RecipesSidebar2")
def RecipesSidebar2():
        return render_template(
        "recipes-sidebar2.html"
    )

@app.route("/UnstuffedCabbage")
def UnstuffedCabbage():
        return render_template(
        "UnstuffedCabbage2.html"
    )

@app.route("/ZucchiniBread")
def ZucchiniBread():
        return render_template(
        "ZucchiniBread.html"
    )
