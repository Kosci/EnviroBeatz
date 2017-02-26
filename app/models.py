from app import db

# Models will go here once written

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(55))
    url = db.Column(db.String(55))
    moods = db.relationship('Mood', backref='song', lazy='dynamic')
    mood_id = db.Column(db.Integer, db.foreign_key('mood.id'))

class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Columns(db.String(55))
    
