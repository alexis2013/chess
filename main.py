import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session, json
from api.models.models import *

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    with app.app_context():
        from api.api import blue
        from api.models.models import db

        app.register_blueprint(blue)
    return app


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


@app.route('/')
def index():
    data = requests.get(url_for("blue.cliente_list", _external=True)).json()
    return render_template("index.html", data=data)


@app.route('/clients', methods=['GET','POST'])
def clients():
    if request.method == 'POST':
        print(json.loads(request.get_data()))
        #data = {"nombre": request.form.get("name"), "apellido": request.form.get("apellido")}
        #requests.patch(url_for("blue.cliente_detail", _external=True, id=request.form.get("id")),data=data)

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
