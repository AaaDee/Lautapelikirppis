from flask_wtf import Form
from wtforms import StringField, IntegerField, validators

class ItemForm(Form):
    name = StringField("Nimi", [validators.DataRequired(message = "Nimi ei saa olla tyhjä")])
    price = IntegerField("Hinta", [validators.DataRequired()])
    description = StringField("Kuvaus")

    class Meta:
        csrf = False