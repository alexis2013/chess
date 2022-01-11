import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, Blueprint

productos = Blueprint("productos", __name__, template_folder="templates")


@productos.route('/products', methods=["GET", 'POST'])
def products():
    if request.method == 'POST':
        headers = {'content-type': 'application/vnd.api+json'}

        data = {"data": {
            "type": "producto",
            "attributes": {
                "descripcion": request.form["newProduct"],
                "precio": int(request.form["newPrice"])
            }
        }
        }
        data = jsonify(data).json
        requests.post(url_for("blue.producto_list", _external=True),
                      json=data, headers=headers)

    data = requests.get(url_for("blue.producto_list", _external=True)).json()
    return render_template("productos.html", data=data)


@productos.route('/new-product', methods=['POST'])
def new_product():
    if request.method == 'POST':
        headers = {'content-type': 'application/vnd.api+json'}

        data = {"data": {
            "type": "producto",
            "attributes": {
                "descripcion": request.form["newProduct"],
                "precio": int(request.form["newPrice"])
            }
        }
        }
        data = jsonify(data).json
        requests.post(url_for("blue.producto_list", _external=True),
                      json=data, headers=headers)

    return redirect(url_for("productos.products"))
