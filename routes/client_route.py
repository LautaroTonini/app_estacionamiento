from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from models.db import db
from models.client import Client
from controllers.client_controller import *

client = Blueprint('client', __name__)

@client.route('/api/clients')
def get_clients():
    return jsonify(obtenerClientes())

@client.route('/api/clients/<int:id>')
def get_client(id):
    client = obtenerClientePorId(id)
    if client:
        return jsonify(client)
    else:
        return jsonify({'error': 'Client not found'}), 404

@client.route('/api/clients/add', methods=['POST'])
def create_client():
    data = request.get_json()
    client, status_code = crearCliente(data)
    return jsonify(client), status_code

@client.route('/api/clients/delete/<int:id>', methods=['DELETE'])
def delete_client(id):
    client, status_code = borrarCliente(id)
    return jsonify(client), status_code

