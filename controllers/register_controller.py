from models.vehicle import Vehicle
from models.category import Category
from models.register import Register
from models.db import db
from datetime import datetime

def asignarCategoria(patente):

    vehiculo = Vehicle.query.get(patente)
    if not vehiculo:
        return None
    if vehiculo.cabina == 0 or vehiculo.puertas is None:
        return "camioneta"
    elif vehiculo.puertas == 0 or vehiculo.puertas is None:
        return "moto"
    else:
        return "auto"

def empezarRegistro(patente):

    categoria = asignarCategoria(patente)

    if not categoria:
        return {"error": "Vehículo no encontrado"}
    
    nuevo_registro = Register(patente=patente)
    nuevo_registro.categoria = categoria
    nuevo_registro.hora_ingreso = datetime.now()
    db.session.add(nuevo_registro)
    db.session.commit()
    return nuevo_registro.serialize()

def terminarRegistro(patente):
    registro = Register.query.filter_by(patente=patente,hora_egreso=None).first()

    if not registro:
        return {"error": "No hay un registro activo para esta patente"}, 404
    hora_egreso = datetime.now()

    horas = (hora_egreso.hour - registro.hora_ingreso.hour) + 1
    categoria = Category.query.filter_by(categoria=registro.categoria).first()

    if not categoria:
        return {"error": "Categoría no encontrada"}, 404

    precio_total = horas * categoria.precio

    registro.hora_egreso = hora_egreso
    registro.precio_total = round(precio_total, 2)

    db.session.commit()

    return registro.serialize(), 200
    
