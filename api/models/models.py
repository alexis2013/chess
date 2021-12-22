from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)























productos = db.Table("productos_compra",
    db.Column("id_compra", db.Integer, db.ForeignKey("compra.id_compra")),
    db.Column("id_producto", db.Integer, db.ForeignKey("producto.id_producto"))
)

class Producto(db.Model):
    __tablename__ = "producto"
    id_producto = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)


class Compra(db.Model):
    __tablename__ = 'compra'
    id_compra = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id_cliente"))
    productos = db.relationship('Producto', secondary=productos, backref="productos", lazy="select")
    total = db.Column(db.Integer)






