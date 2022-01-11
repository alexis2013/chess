import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, Blueprint

clientes = Blueprint("clientes", __name__, template_folder="templates")


@clientes.route('/clients', methods=["GET", 'POST'])
def clients():
    if request.method == 'POST':
        headers = {'content-type': 'application/vnd.api+json'}

        data = {"data": {
                    "id": request.form["id"],
                    "type": "cliente",
                    "attributes": {
                        "nombre": request.form["name"],
                        "apellido": request.form["lastname"]
                          }
                    }
                }
        data = jsonify(data).json
        requests.patch(url_for("blue.cliente_detail", _external=True, id=request.form.get("id")),
                       json=data, headers=headers)

    data = requests.get(url_for("blue.cliente_list", _external=True)).json()

    return render_template("clientes.html", data=data)


@clientes.route('/new-client', methods=['POST'])
def new_clients():
    if request.method == 'POST':
        headers = {'content-type': 'application/vnd.api+json'}

        data = {"data" :{
                    "type" : "cliente",
                    "attributes": {
                        "nombre" : request.form["newName"],
                        "apellido" : request.form["newLastName"]
                          }
                    }
                }
        data = jsonify(data).json
        requests.post(url_for("apiBlueprint.cliente_list", _external=True),
                       json=data, headers=headers)

    return redirect(url_for("clientes.clients"))