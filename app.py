from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import PetForm
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'adoption'
# debug = DebugToolbarExtension(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

connect_db(app)


@app.route('/')
def homepage():
    """lists the pets, photo and availability"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def enroll():
    """adds new pet to db"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species,
                      photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash('Pet added, welcome aboard')
        return redirect('/')
    else:
        return render_template('pet-form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_and_edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash("IT's updated!")
        print('passed')
        return redirect('/')
    else:
        print('not validated')
        return render_template('show-pet.html', pet=pet, form=form)
