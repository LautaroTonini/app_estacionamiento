from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.location import Location
from controllers.location_controller import *

location = Blueprint('location', __name__)

@location.route('/api/locations')
def get_locations():
    return jsonify(obtenerEstacionamientos())

@location.route('/api/locations/<int:num_espacio>')
def get_location(num_espacio):
    location = obtenerEstacionamientoPorId(num_espacio)
    if location:
        return jsonify(location)
    else:
        return jsonify({'error': 'Location not found'}), 404
    
@location.route('/api/locations/empty')
def get_empty_location():
    location = obtenerEstacionamientoVacio()
    if location:
        return jsonify(location)
    else:
        return jsonify({'error': 'No empty locations available'}), 404

@location.route('/api/locations/occupy/<int:num_espacio>', methods=['POST'])
def occupy_location(num_espacio):
    location, status_code = ocuparEstacionamiento(num_espacio)
    return jsonify(location), status_code

@location.route('/api/locations/vacate/<int:num_espacio>', methods=['POST'])
def vacate_location(num_espacio):
    location, status_code = desocuparEstacionamiento(num_espacio)
    return jsonify(location), status_code
    
