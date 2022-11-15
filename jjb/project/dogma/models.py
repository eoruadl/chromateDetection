from dogma import db

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Lot = db.Column(db.Integer, nullable=False)
    Time = db.Column(db.DateTime, nullable=False)
    pH = db.Column(db.Float, nullable=False)
    Temp = db.Column(db.Float, nullable=False)
    Voltage = db.Column(db.Float, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)