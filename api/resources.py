from flask_rest_jsonapi import  ResourceDetail, ResourceList, ResourceRelationship
from api.schema.schema import *
from api.models.models import *


class ClienteDetail(ResourceDetail):
    schema = ClienteSchema
    data_layer = {"session" : db.session,
                  "model" : Cliente}


class ClienteList(ResourceList):
    schema = ClienteSchema
    data_layer = {"session": db.session,
                  "model": Cliente}




