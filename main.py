import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from api.models.models import *

from clientes import clientes
from productos import productos


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    with app.app_context():
        from api.api import blue

        app.register_blueprint(blue)
        app.register_blueprint(clientes)
        app.register_blueprint(productos)
    return app


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


@app.route('/')
def index():
    return redirect(url_for("clientes.clients"))


if __name__ == '__main__':
    app.run(debug=True)
