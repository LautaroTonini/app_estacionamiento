from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.vehicle import Vehicle
from controllers.vehicle_controller import *

vehicle = Blueprint('vehicle', __name__)

@vehicle.route('/api/vehicles')
def get_vehicles():
    return jsonify(obtenerVehiculo())