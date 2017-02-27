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
    
class Environment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	gyro_x = db.Column(db.Float)
	gyro_y = db.Column(db.Float)
	gyro_z = db.Column(db.Float)
	sensor_temp = db.Column(db.Float)
	room_temp = db.Column(db.Float)
	compass_x = db.Column(db.Float)
	compass_y = db.Column(db.Float)
	compass_z = db.Column(db.Float)
	accel_x = db.Column(db.Float)
	accel_y = db.Column(db.Float)
	accel_z = db.Column(db.Float)
	air_pressure = db.Column(db.Float)
	light = db.Column(db.Float)
	
class SongTemperature(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	song_id = db.Column(db.Integer, db.foreign_key('song.id')
	temp_min = db.Column(db.Float)
	temp_max = db.Column(db.Float)
	
class SongLight(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	song_id = db.Column(db.Integer, db.foreign_key('song.id')
	light_min = db.Column(db.Float)
	light_max = db.Column(db.Float)
	
    