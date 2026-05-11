from models.location import Location
from models.db import db

def obtenerEstacionamientos():
    locations = Location.query.all()
    return [location.serialize() for location in locations], 200

def obtenerEstacionamientoPorId(num_espacio):
    location = Location.query.get(num_espacio)
    if location:
        return location.serialize(), 200
    else:
        return "Estacionamiento no encontrado", 404

def obtenerEstacionamientoVacio():
    location = Location.query.filter_by(ocupado=False).all()
    if location:
        return [location.serialize() for location in location], 200
    else:
        return "No hay estacionamientos vacios", 404

def ocuparEstacionamiento(num_espacio):
    location = Location.query.get(num_espacio)
    if not location:
        return ("error: Estacionamiento no encontrado"), 404
    if location.ocupado:
        return ("error: El estacionamiento ya está ocupado"), 400
    if location and not location.ocupado:
        location.ocupado = True
        db.session.commit()
        return location.serialize(), 200

def desocuparEstacionamiento(num_espacio):
    location = Location.query.get(num_espacio)
    if not location:
        return ("error: Estacionamiento no encontrado"), 404
    if not location.ocupado:
        return ("error: El estacionamiento ya está desocupado"), 400
    if location and location.ocupado:
        location.ocupado = False
        db.session.commit()
        return location.serialize(), 200