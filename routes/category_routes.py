from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from controllers.client_controller import borrarCliente, crearCliente
from models import client
from models.db import db
from models.category import Category
from controllers.category_controller import *

category = Blueprint('category', __name__)

@category.route('/api/categories')
def get_categories():
    return jsonify(obtenerCategorias())

@category.route('/api/categories/<string:nombre>')
def get_category(nombre):
    category = obtenerCategoriaPorNombre(nombre)
    if category:
        return jsonify(category)
    else:
        return jsonify({'error': 'Category not found'}), 404

@category.route('/api/categories/add', methods=['POST'])
def create_category():
    data = request.get_json()
    category, status_code = crearCategoria(data)
    return jsonify(category), status_code

@category.route('/api/categories/delete/<categoria>', methods=['DELETE'])
def delete_category(categoria):
    category, status_code = borrarCategoria(categoria)
    return jsonify(category), status_code

