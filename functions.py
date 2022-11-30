from datetime import datetime

def serialize_sensor_data(data):
    sensor_data = []

    for record in data:
        sensor_data.append({
            'co2': record.co2,
            'co2_status': record.co2_status,
            'temperature': record.temperature,
            'temperature_status': record.temperature_status,
            'humidity': record.humidity,
            'humidity_status': record.humidity_status,
            'created_at': datetime.strftime(record.created_at, '%d-%m-%Y %H:%M'),
        })

    return sensor_data