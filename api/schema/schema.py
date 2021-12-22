from marshmallow_jsonapi.flask import Schema, Relationship
from api.models import *
from marshmallow_jsonapi import fields


class ClienteSchema(Schema):
    class Meta:
        type_ = "cliente"
        self_view = "blue.cliente_detail"
        self_view_kwargs = {"id" : "<id>"}

    id = fields.Integer(as_string=True, dump_only=True, attribute="id_cliente")
    nombre = fields.String()
    apellido = fields.String()













class ProductoSchema(Schema):
    class Meta:
        type_ = "producto"
        self_view = "blue.producto_detail"
        self_view_kwargs = {"id" : "<id>"}

    id = fields.Integer(as_string=True, dump_only=True, attribute="id_producto")
    descripcion = fields.String()
    precio = fields.Integer()


class CompraSchema(Schema):
    class Meta:
        type_ = "compra"
        self_view = "blue.compra_detail"
        self_view_kwargs = {"id" : "<id>"}

    id = fields.Integer(as_string=True, dump_only=True, attribute="id_compra")
    id_cliente = fields.Integer()
    Productos = fields.Relationship(type_="producto",
                                    many=True,
                                    related_view="productos/compra",
                                    related_view_kwargs={"id_compra":"<id>"}
                                    )



