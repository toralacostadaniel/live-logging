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
            'created_at': datetime.strptime(record.created_at, '%Y-%m-%d %H:%M'),
        })

    return sensor_data