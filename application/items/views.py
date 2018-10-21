from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.items.models import Item
from application.items.forms import ItemForm, GameToItemForm

from application.games.models import Game

# Helper function for updating default arguments
def edit_defaults(item, form):
    form.name.default = item.name
    form.price.default = item.price
    form.description.default = item.description
    form.process()

def add_gameName_to_item(item, gameName):
    game = Game.query.filter_by(name = gameName).first()

    item.games.append(game)
    db.session.commit()

# Edit-template is rendered multiple times, so it's grouped here
def edit_template(item, itemForm, gameForm = 'default', errorMessage = ''):
    if gameForm == 'default':
        gameForm = GameToItemForm()
    return render_template('items/edit.html', item = item, itemForm = itemForm, gameForm = gameForm, error = errorMessage)

def game_already_in_item_error_message():
        errorMessage = '''
                        Lisäämäsi peli on jo myyntikohteessa. Jos haluat myydä useamman kopion samasta
                        pelistä, luo jokaiselle oma myyntikohde
                        '''
        return errorMessage

@app.route('/items', methods=['GET'])
def items_index():
    return render_template('items/list.html', 
                           items = Item.query.filter_by(sold = False),
                           items_total = Item.items_unsold_total())

@app.route('/items/new/', methods=['GET'])
@login_required
def items_form():
    return render_template('items/new.html', form = ItemForm())

@app.route('/items/new/', methods=['POST'])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template('items/new.html', form = form)

    new_item = Item(form.name.data, 
                    form.description.data,
                    form.price.data)
    
    new_item.account_id = current_user.id
    gameName = form.gameName.data

    db.session().add(new_item)
    add_gameName_to_item(new_item, gameName)

    db.session().commit()
  
    return redirect(url_for('item_add_games', item_id = new_item.id))

@app.route('/items/new/addgames/<item_id>', methods=['GET'])
@login_required
def item_add_games(item_id):

    form = GameToItemForm(request.form)
    new_item = Item.query.get(item_id)

    return render_template('items/addgames.html', form = form, item = new_item, error = '')

@app.route('/items/new/addgames/<item_id>', methods=['POST'])
@login_required
def item_submit_game(item_id):
    form = GameToItemForm(request.form)
    item = Item.query.get(item_id)

    if not form.validate():
        return render_template('items/addgames.html', form = form, item = item, error = '')
    
    gameName = form.name.data

    if Item.check_game_in_item(item, gameName):
        errorMessage = game_already_in_item_error_message()
        return render_template('items/addgames.html', form = form, item = item, error = errorMessage)
    
    
    add_gameName_to_item(item, gameName)

    return redirect(url_for('item_add_games', item_id = item.id))


@app.route('/items/edit/addgames/<item_id>', methods=['POST'])
@login_required
def item_submit_game_edit(item_id):
    gameForm = GameToItemForm(request.form)
    item = Item.query.get(item_id)

    itemForm = ItemForm()
    edit_defaults(item, itemForm)

    if not gameForm.validate():
        return edit_template(item, itemForm, gameForm = gameForm)
    
    gameName = gameForm.name.data

    if Item.check_game_in_item(item, gameName):
        errorMessage = game_already_in_item_error_message()
        return edit_template(item, itemForm, gameForm = gameForm, errorMessage = errorMessage)
    
    add_gameName_to_item(item, gameName)

    return edit_template(item, itemForm , gameForm = gameForm)

@app.route('/items/sold/<item_id>', methods=['POST'])
@login_required
def item_mark_as_sold(item_id):
    item = Item.query.get(item_id)
    item.sold = True
    db.session.commit()
    return redirect(url_for('auth_mypage'))


@app.route('/items/edit/<item_id>', methods=['GET', 'POST'])
@login_required
def item_edit(item_id):  
    edited_item = Item.query.get(item_id)
    edit_form = ItemForm()

    if request.method == 'GET': 
        edit_defaults(edited_item, edit_form)

        

    else:
        edit_form = ItemForm(request.form)

        if not edit_form.validate():
            return edit_template(edited_item, edit_form)
        
        edited_item.name = edit_form.name.data
        edited_item.price = edit_form.price.data
        edited_item.description = edit_form.description.data

    # Return to the same edit page in both methods
    return edit_template(edited_item, edit_form)


@app.route('/items/edit/deletegame/<item_id>/<game_id>', methods=['POST'])
@login_required
def delete_game_in_item(item_id, game_id):
    
    item = Item.query.get(item_id)

    if (len(item.games) == 1):
        errorMessage = 'Myyntikohteessa on oltava vähintään yksi peli'
        form = ItemForm()
        edit_defaults(item, form)
        
        return edit_template(item, form, errorMessage = errorMessage)

    Item.delete_game(item_id, game_id)

    db.session.commit()

    form = ItemForm()
    edit_defaults(item, form)
    

        
    return edit_template(item, form) 

@app.route('/items/delete/<item_id>/<path>', methods=['POST'])
@login_required
def item_delete(item_id, path):
    item =Item.query.get(item_id)
    
    db.session().delete(item)
    db.session().commit()

    return redirect(url_for('auth_mypage'))


'''
@app.route('/items/check/<item_id>/', methods=['POST'])
@login_required
def item_check_edit(item_id):
    edited_item = Item.query.get(item_id)

    if (len(edited_item.games) == 0):
        errorMessage = 'Myyntikohteessa on oltava vähintään yksi peli'
        edit_form = ItemForm()
        edit_defaults(edited_item, edit_form)
        
        return render_template('items/edit.html', item = edited_item, form = edit_form, error = errorMessage)
    
    db.session.commit()
    
    return redirect(url_for('auth_mypage'))
'''