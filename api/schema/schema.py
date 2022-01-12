from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow import pre_load
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
    compras = Relationship(
                            self_view="client_shop",
                            self_view_kwargs= {"id": "id"},
                            related_view="compra_list",
                            related_view_kwargs= {"id", "id"},
                            many= True,
                            schema= "CompraSchema",
                            type_= "compra"
                            )

    @pre_load
    def remove_id_before_deserializing(self, data, **kwargs):
        """
        We don't want to allow editing ID on POST / PATCH

        Related issues:
        https://github.com/AdCombo/flask-combo-jsonapi/issues/34
        https://github.com/miLibris/flask-rest-jsonapi/issues/193
        """
        if 'id' in data:
            del data['id']
        return data


class ProductoSchema(Schema):
    class Meta:
        type_ = "producto"
        self_view = "blue.producto_detail"
        self_view_kwargs = {"id" : "<id>"}

    id = fields.Integer(as_string=True, dump_only=True, attribute="id_producto")
    descripcion = fields.String()
    precio = fields.Integer()

    @pre_load
    def remove_id_before_deserializing(self, data, **kwargs):
        """
        We don't want to allow editing ID on POST / PATCH

        Related issues:
        https://github.com/AdCombo/flask-combo-jsonapi/issues/34
        https://github.com/miLibris/flask-rest-jsonapi/issues/193
        """
        if 'id' in data:
            del data['id']
        return data


class CompraSchema(Schema):
    class Meta:
        type_ = "compra"
        self_view = "blue.compra_detail"
        self_view_kwargs = {"id" : "<id>"}

    id = fields.Integer(as_string=True, dump_only=True, attribute="id_compra")
    id_cliente = fields.Integer()
    productos = fields.Integer()


    @pre_load
    def remove_id_before_deserializing(self, data, **kwargs):
        """
        We don't want to allow editing ID on POST / PATCH

        Related issues:
        https://github.com/AdCombo/flask-combo-jsonapi/issues/34
        https://github.com/miLibris/flask-rest-jsonapi/issues/193
        """
        if 'id' in data:
            del data['id']
        return data











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



