from app import application

from flask import render_template

from models import *

from functions import *

@application.route('/', methods=['GET'])
def index():
    LIMIT = 10

    sensor_one_data = SensorOne.query.with_entities(
        SensorOne.co2,
        SensorOne.co2_status,
        SensorOne.temperature,
        SensorOne.temperature_status,
        SensorOne.humidity,
        SensorOne.humidity_status,
        SensorOne.created_at,
    ).order_by(SensorOne.created_at.desc()).limit(LIMIT).all()
    
    sensor_one_data = serialize_sensor_data(sensor_one_data)

    sensor_two_data = SensorTwo.query.with_entities(
        SensorTwo.co2,
        SensorTwo.co2_status,
        SensorTwo.temperature,
        SensorTwo.temperature_status,
        SensorTwo.humidity,
        SensorTwo.humidity_status,
        SensorTwo.created_at,
    ).order_by(SensorTwo.created_at.desc()).limit(LIMIT).all()

    sensor_two_data = serialize_sensor_data(sensor_two_data)

    sensor_three_data = SensorThree.query.with_entities(
        SensorThree.co2,
        SensorThree.co2_status,
        SensorThree.temperature,
        SensorThree.temperature_status,
        SensorThree.humidity,
        SensorThree.humidity_status,
        SensorThree.created_at,
    ).order_by(SensorThree.created_at.desc()).limit(LIMIT).all()

    sensor_three_data = serialize_sensor_data(sensor_three_data)

    return render_template('index.html', data={
        'sensor_one': sensor_one_data,
        'sensor_two': sensor_two_data,
        'sensor_three': sensor_three_data,
    })