
from models.db import db

class Category(db.Model):

    __tablename__ = 'category'

    categoria = db.Column(db.String(45), unique=True, nullable=False, primary_key=True)
    precio = db.Column(db.Integer, nullable=False)
    

    def __init__(self, categoria, precio):
        self.categoria = categoria
        self.precio = precio

    def serialize(self):
        return {
            'categoria': self.categoria,
            'precio': self.precio
        }    