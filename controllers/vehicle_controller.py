from models.vehicle import Vehicle
from models.db import db

def obtenerVehiculo():
    vehicle = Vehicle.query.all()
    return [vehicle.serialize() for vehicle in vehicle]

def registrarVehiculo(**data):
    nuevoVehiculo = Vehicle(**data)
    vehiculoExiste = Vehicle.query.get(nuevoVehiculo.patente)
    if vehiculoExiste:
        return "Error: La patente ya existe", 400
    elif not vehiculoExiste:
        db.session.add(nuevoVehiculo)
        db.session.commit()
        return nuevoVehiculo.serialize(), 201
    else:
        return "Error inesperado", 500
    
def borrarvehiculo(patente):
    vehicle = Vehicle.query.get(patente)
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return "", 204
    else:
        return "Patente no encontrada", 404