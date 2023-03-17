from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
        #De esta manera se agregan campos en una tabla
                   #tipoDato   #Indica que es llave primaria
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(100))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

class Profesores(db.Model):
    __tablename__ = 'profesor'
        #De esta manera se registran los campos de una tabla
                   #tipoDato   #Indica que es llave primaria
    id        = db.Column(db.Integer, primary_key=True)
    nombre    = db.Column(db.String(50))
    apellidos = db.Column(db.String(100))
    materia   = db.Column(db.String(30))
    grupo     = db.Column(db.String(40))
    estatus   = db.Column(db.Integer)
