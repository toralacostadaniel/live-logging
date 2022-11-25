from app import db

class SensorOne(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    co2 = db.Column(db.Numeric(7, 3), nullable=False)
    co2_status = db.Column(db.SmallInteger, nullable=False)
    humidity = db.Column(db.Numeric(5, 2), nullable=False)
    humidity_status = db.Column(db.SmallInteger, nullable=False)
    temperature = db.Column(db.Numeric(5, 2), nullable=False)
    temperature_status = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class SensorTwo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    co2 = db.Column(db.Numeric(7, 3), nullable=False)
    co2_status = db.Column(db.SmallInteger, nullable=False)
    humidity = db.Column(db.Numeric(5, 2), nullable=False)
    humidity_status = db.Column(db.SmallInteger, nullable=False)
    temperature = db.Column(db.Numeric(5, 2), nullable=False)
    temperature_status = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class SensorThree(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    co2 = db.Column(db.Numeric(7, 3), nullable=False)
    co2_status = db.Column(db.SmallInteger, nullable=False)
    humidity = db.Column(db.Numeric(5, 2), nullable=False)
    humidity_status = db.Column(db.SmallInteger, nullable=False)
    temperature = db.Column(db.Numeric(5, 2), nullable=False)
    temperature_status = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)