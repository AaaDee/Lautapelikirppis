from flask_wtf import Form
from wtforms import StringField, IntegerField, validators

class GameForm(Form):
    name = StringField("Nimi", [validators.DataRequired(message = "Nimi ei saa olla tyhjä")])
    bgg = IntegerField("BGG-tunnus", [validators.Optional()])
    


    class Meta:
        csrf = False