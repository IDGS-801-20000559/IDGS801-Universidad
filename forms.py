from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('ID')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    grupo = StringField('Grupo')
    materia = StringField('Materia')
    busqueda = StringField('Escribe para realizar una busqueda')
    email = EmailField('Correo')