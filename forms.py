from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional, Email

species = ['dog', 'cat', 'rabbit', 'horse',
           'racoon', 'parrot', 'dolphin', 'lizard']


class PetForm(FlaskForm):
    name = StringField("Pet's name")
    species = SelectField('Species', choices=[(sp, sp) for sp in species])
    photo_url = URLField('Link to image')
    age = IntegerField(validators=[Optional()])
    notes = StringField(validators=[Optional()])
    available = BooleanField(validators=[Optional()])
