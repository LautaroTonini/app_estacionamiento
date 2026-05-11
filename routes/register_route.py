from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.register import Register
from controllers.register_controller import *

register = Blueprint('register', __name__)

@register.route('/api/registers/create/<patente>',methods=['POST'])
def create_register(patente):

    registro = empezarRegistro(patente)

    return jsonify(registro), 201

@register.route('/api/registers/finish/<patente>',methods=['PUT'])

def finish_register(patente):

    registro, status = terminarRegistro(patente)

    return jsonify(registro), status