from models.db import db


class Register(db.Model):

    __tablename__ = 'register'

    id_registro = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    patente = db.Column(
        db.String(45),
        nullable=False
    )

    categoria = db.Column(
        db.String(45),
        nullable=False
    )

    hora_ingreso = db.Column(
        db.DateTime,
        nullable=False
    )

    hora_egreso = db.Column(
        db.DateTime,
        nullable=True
    )

    precio_total = db.Column(
        db.Float,
        nullable=True
    )

    def __init__(self, patente):
        self.patente = patente

    def serialize(self):
        return {
            "id_registro": self.id_registro,
            "patente": self.patente,
            "categoria": self.categoria,
            "hora_ingreso": self.hora_ingreso,
            "hora_egreso": self.hora_egreso,
            "precio_total": self.precio_total
        }