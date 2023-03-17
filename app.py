from db import get_connection
from flask import Flask, redirect, jsonify, render_template
from flask import request
from flask import url_for
import forms
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos
from maestros.routes import maestros
from alumnos.routes import alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

# Registra la blueprint
app.register_blueprint(maestros)
app.register_blueprint(alumnos)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)