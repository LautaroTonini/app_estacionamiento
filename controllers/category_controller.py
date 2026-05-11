from models.category import Category
from models.client import Client
from models.db import db

def obtenerCategorias():
    categories = Category.query.all()
    return [category.serialize() for category in categories]

def obtenerCategoriaPorNombre(categoria):
    category = Category.query.get(categoria)
    if category:
        return category.serialize()
    else:
        return "Categoria no encontrada", 404 
    
def crearCategoria(data):
    categoriaExiste = Category.query.get(data['categoria'])
    if categoriaExiste:
        return "Error: La categoría ya existe", 400
    categoria_nueva = Category(**data)
    db.session.add(categoria_nueva)
    db.session.commit()
    return categoria_nueva.serialize(), 201

def borrarCategoria(nombre):
    categoria = Category.query.get(nombre)

    if not categoria:
        return {"error": "Categoria no encontrada"}, 404

    db.session.delete(categoria)

    db.session.commit()

    return '', 204