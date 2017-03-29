from app.models import Environment

# get the last 10 and average
def averageEnvironmentData():
    gyro_x = 0
    gyro_y = 0
    gyro_z = 0
    sensor_temp = 0
    room_temp = 0
    compass_x = 0
    compass_y = 0
    compass_z = 0
    accel_x = 0
    accel_y = 0
    accel_z = 0
    air_pressure = 0
    light = 0

    data = Environment.query.order_by(-Environment.id.desc()).limit(10)
    for environment in data:
        gyro_x += environment.gyro_x
        gyro_y += environment.gyro_y
        gyro_z += environment.gyro_z
        sensor_temp += environment.sensor_temp
        room_temp += environment.room_temp
        compass_x += environment.compass_x
        compass_y += environment.compass_y
        compass_z += environment.compass_z
        accel_x += environment.accel_x
        accel_y += environment.accel_y
        air_pressure += environment.air_pressure
        light += environment.light

    return Environment(gyro_x = gyro_x / 10,
                        gyro_y = gyro_y / 10,
                        gyro_z = gyro_z / 10,
                        sensor_temp = sensor_temp / 10,
                        room_temp = room_temp / 10,
                        compass_x = compass_x / 10,
                        compass_y = compass_y / 10,
                        compass_z = compass_z / 10,
                        accel_x = accel_x / 10,
                        accel_y = accel_y / 10,
                        accel_z = accel_z / 10,
                        air_pressure = air_pressure / 10,
                        light = light / 10
                    )

					
def getGyroData():
	gyros = {}
	data = Environment.query.order_by(-Environment.id.desc()).limit(4)
	for environment in data:
		gyros["x"].append(environment.gyro_x)
		gyros["y"].append(environment.gyro_y)
		gyros["z"].append(environment.gyro_z)
	return gyros
	