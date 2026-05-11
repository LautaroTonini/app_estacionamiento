from models.db import db

class Vehicle(db.Model):

    __tablename__ = 'vehicle'

    patente = db.Column(db.String(45), unique=True, nullable=False, primary_key=True)
    año_modelo = db.Column(db.String(45), nullable=False)
    marca = db.Column(db.String(45), nullable=False)
    puertas = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(45), nullable=False)
    combustible = db.Column(db.String(45), nullable=False)

    def __init__(self, ano_modelo, marca, puertas, color, patente, combustible):
        self.patente = patente
        self.ano_modelo = ano_modelo
        self.marca = marca
        self.puertas = puertas
        self.color = color
        self.combustible = combustible

    def serialize(self):
        return {
            'patente': self.patente,
            'ano_modelo': self.ano_modelo,
            'marca': self.marca,
            'puertas': self.puertas,
            'color': self.color,
            'combustible': self.combustible
        }    