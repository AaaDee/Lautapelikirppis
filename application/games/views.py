from application import app, db
from flask import redirect, render_template, request, url_for
from application.games.models import Game
from application.games.forms import GameForm

@app.route('/games', methods=['GET'])
def games_index():
    return render_template('games/list.html', games = Game.query.all(), error = "")

@app.route('/games/new/')
def games_form():
    return render_template('games/new.html', form = GameForm())

@app.route('/games/edit/<game_id>', methods=['GET'])
def games_edit(game_id):
    edited_game = Game.query.get(game_id)
    return render_template('games/edit.html', game = edited_game, form = GameForm())

@app.route('/games/', methods=['POST'])
def games_create():
    form = GameForm(request.form)

    if not form.validate():
        return render_template('games/new.html', form = form)

    new_game = Game(form.name.data)
    new_game.bgg = form.bgg.data

    db.session().add(new_game)
    db.session().commit()
  
    return redirect(url_for('games_index'))


@app.route('/games/edit/<game_id>', methods=['POST'])
def games_edit_submit(game_id):
    form = GameForm(request.form)
    g = Game.query.get(game_id)

    if not form.validate():
            return render_template('games/edit.html', form = form, game=g)

    g.name = form.name.data
    g.bgg = form.bgg.data

    db.session().commit()

    return redirect(url_for('games_index'))

@app.route('/games/delete/<game_id>', methods=['POST'])
def games_delete(game_id):
    game = Game.query.get(game_id)
    
    if (game.is_game_in_items()):
        error_message = "Poisto ei ole sallittu, koska peli on käytössä myynnissä olevassa tai myydyssä kohteessa. Poista myyntikohteet ensin."
        return render_template('games/list.html', games = Game.query.all(), error = error_message)

    db.session().delete(game)
    db.session().commit()

    return redirect(url_for('games_index'))