from flask_rest_jsonapi import  ResourceDetail, ResourceList, ResourceRelationship
from api.schema.schema import *
from api.models.models import *


class ClienteDetail(ResourceDetail):

    def before_update_object(self, *args, **kwargs):
        print(args)
        print(kwargs)

    schema = ClienteSchema
    data_layer = {"session" : db.session,
                  "model" : Cliente,
                  "methods" : {
                      "before_patch" : before_update_object
                    }
                  }


class ClienteList(ResourceList):
    schema = ClienteSchema
    data_layer = {"session": db.session,
                  "model": Cliente}


class ProductoDetail(ResourceDetail):

    def before_update_object(self, *args, **kwargs):
        print(args)
        print(kwargs)

    schema = ProductoSchema
    data_layer = {"session" : db.session,
                  "model" : Producto,
                  "methods" : {
                      "before_patch" : before_update_object
                    }
                  }


class ProductoList(ResourceList):
    schema = ProductoSchema
    data_layer = {"session": db.session,
                  "model": Producto}






