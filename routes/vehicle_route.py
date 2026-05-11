from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.vehicle import Vehicle
from controllers.vehicle_controller import *

vehicle = Blueprint('vehicle', __name__)

@vehicle.route('/api/vehicles')
def get_vehicles():
    return jsonify(obtenerVehiculo())

@vehicle.route('/api/vehicles/create', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    try:
        return registrarVehiculo(data)
    except IntegrityError:
        db.session.rollback()
        return "Error: La patente ya existe", 400
    except Exception:
        db.session.rollback()
        return "Error inesperado", 500