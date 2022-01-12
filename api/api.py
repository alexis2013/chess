from flask import Blueprint, current_app as app
from api.resources import *
from flask_rest_jsonapi import Api

blue = Blueprint('blue', __name__)

api = Api(app, blue)

api.route(ClienteDetail, "cliente_detail", "/cliente/<id>")
api.route(ClienteList, "cliente_list", "/clientes")

api.route(ProductoDetail, "producto_detail", "/product/<id>")
api.route(ProductoList, "producto_list", "/productos")

api.route(ClienteRelationship, "client_shop", "/cliente/<id>/relationship/owner")