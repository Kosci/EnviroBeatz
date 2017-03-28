from app.models
from app.home import data

def skip_song():
	gyros = data.getGyroData()
	
	is_shaking = False
	keys = gyros.keys()
	for key in keys():
		pos_orientation = True
		for coord in gyros[key]:
			if coord<0 and pos_orientation:
				pos_orientation = False
				is_shaking = True
			elif coord>0 and !pos_orientation:
				pos_orientation = True
				is_shaking = True