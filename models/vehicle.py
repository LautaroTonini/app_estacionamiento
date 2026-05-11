from models.db import db

class Vehicle(db.Model):

    __tablename__ = 'vehicle'

    patente = db.Column(db.String(45), unique=True, nullable=False, primary_key=True)
    ano_modelo = db.Column(db.Integer, nullable=False)
    marca = db.Column(db.String(45), nullable=False)
    puertas = db.Column(db.Integer, nullable=True)
    color = db.Column(db.String(45), nullable=False)
    cabina = db.Column(db.String(45), nullable=True)

    def __init__(self, ano_modelo, marca, puertas, color, patente, cabina):
        self.patente = patente
        self.ano_modelo = ano_modelo
        self.marca = marca
        self.puertas = puertas
        self.color = color
        self.cabina = cabina

    def serialize(self):
        return {
            'patente': self.patente,
            'ano_modelo': self.ano_modelo,
            'marca': self.marca,
            'puertas': self.puertas,
            'color': self.color,
            'cabina': self.cabina,
        }