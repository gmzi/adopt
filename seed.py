from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species="dog", available=False, photo_url='https://img.etimg.com/thumb/msid-72951938,width-650,imgsize-579705,,resizemode-4,quality-100/the-owners-can-also-make-a-few-changes-like-increasing-or-decreasing-a-specific-substance-it-is-better-to-minimise-treats-during-this-season-as-it-contributes-to-the-weight-.jpg')
bowser = Pet(name='Bowser', species="dog", photo_url='https://img.etimg.com/thumb/msid-72951938,width-650,imgsize-579705,,resizemode-4,quality-100/the-owners-can-also-make-a-few-changes-like-increasing-or-decreasing-a-specific-substance-it-is-better-to-minimise-treats-during-this-season-as-it-contributes-to-the-weight-.jpg')
spike = Pet(name='Spike', species="porcupine", photo_url='https://img.etimg.com/thumb/msid-72951938,width-650,imgsize-579705,,resizemode-4,quality-100/the-owners-can-also-make-a-few-changes-like-increasing-or-decreasing-a-specific-substance-it-is-better-to-minimise-treats-during-this-season-as-it-contributes-to-the-weight-.jpg')

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit to database
db.session.commit()
