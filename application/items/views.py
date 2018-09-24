from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
from application.items.forms import ItemForm

@app.route("/items", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
def items_form():
    return render_template("items/new.html", form = ItemForm())

@app.route("/items/", methods=["POST"])
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)

    item = Item(form.name.data, 
        form.price.data,
        form.description.data)


    db.session().add(item)
    db.session().commit()
  
    return redirect(url_for("items_index"))