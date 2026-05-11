from models.vehicle import Vehicle
from models.db import db

class Location(db.Model):

    __tablename__ = 'location'

    num_espacio = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    patente = db.Column(db.String(45), db.ForeignKey('vehicle.patente'), nullable=True)
    ocupado = db.Column(db.Boolean, nullable=False)

    def __init__(self, num_espacio, patente, ocupado):
        self.num_espacio = num_espacio
        self.patente = patente
        self.ocupado = ocupado

    def serialize(self):
        return {
            'num_espacio': self.num_espacio,
            'patente': self.patente,
            'ocupado': self.ocupado
        }    