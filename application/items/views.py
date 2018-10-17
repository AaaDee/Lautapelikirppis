from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.items.models import Item
from application.items.forms import ItemForm, GameToItemForm

from application.games.models import Game

@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", 
                           items = Item.query.filter_by(sold = False),
                           items_total=Item.items_total())

@app.route("/items/new/")
@login_required
def items_form():
    return render_template("items/new.html", form = ItemForm())

@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)

    new_item = Item(form.name.data, 
                    form.description.data,
                    form.price.data)
    
    new_item.account_id = current_user.id


    db.session().add(new_item)
    db.session().commit()
  
    return redirect(url_for("item_add_games", item_id = new_item.id))

@app.route("/items/new/addgames/<item_id>", methods=["GET"])
@login_required
def item_add_games(item_id):

    form = GameToItemForm(request.form)
    new_item = Item.query.get(item_id)

    return render_template("items/addgames.html", form = form, item = new_item)

@app.route("/items/new/addgames/<item_id>", methods=["POST"])
@login_required
def item_submit_game(item_id):
    form = GameToItemForm(request.form)
    new_item = Item.query.get(item_id)

    if not form.validate():
        return render_template("items/addgames.html", form = form, item = new_item)
    
    # temp solution, when updated also update the first game loop in the beginning
    gameName = form.name.data
    game = Game.query.filter_by(name = gameName).first()

    new_item.games.append(game)
    db.session.commit()

    return redirect(url_for("item_add_games", item_id = new_item.id))

@app.route("/items/sold/<item_id>", methods=["POST"])
@login_required
def item_mark_as_sold(item_id):
    item = Item.query.get(item_id)
    item.sold = True
    db.session.commit()
    return redirect(url_for("auth_mypage"))
