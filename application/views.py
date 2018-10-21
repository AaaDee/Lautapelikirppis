from flask import render_template
from application import app

from application.items.models import Item

@app.route("/")
def index():

    did_you_know = Item.most_active_city()

    dykCity = did_you_know[0]['Place']
    dykAmount = did_you_know[0]['Amount']

    return render_template("index.html", dykCity = dykCity, dykAmount = dykAmount)