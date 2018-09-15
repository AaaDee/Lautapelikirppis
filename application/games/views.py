from application import app, db
from flask import redirect, render_template, request, url_for
from application.games.models import Game

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())

@app.route("/games/new/")
def games_form():
    return render_template("games/new.html")

@app.route("/games/edit/<game_id>", methods=["GET"])
def games_edit(game_id):
    g = Game.query.get(game_id)
    return render_template("games/edit.html", game = g)

@app.route("/games/", methods=["POST"])
def games_create():
    g = Game(request.form.get("name"), request.form.get("bgg"))

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))


@app.route("/games/edit/<game_id>", methods=["POST"])
def games_edit_submit(game_id):
    g = Game.query.get(game_id)
    
    g.name = request.form.get("name")
    g.bgg = request.form.get("bgg")

    db.session().commit()

    return redirect(url_for("games_index"))

@app.route("/games/delete/<game_id>", methods=["POST"])
def games_delete(game_id):
    g = Game.query.get(game_id)
    
    db.session().delete(g)
    db.session().commit()

    return redirect(url_for("games_index"))