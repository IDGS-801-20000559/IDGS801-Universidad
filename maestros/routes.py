from flask import render_template, redirect
from flask import request
from flask import url_for
from models import Profesores
import forms
from flask import Blueprint
import main

maestros = Blueprint('maestros', __name__)

@maestros.route("/profesores", methods = ['GET', 'POST'])
def profesores():
    create_form = forms.UserForm(request.form)
    # Para poder realizar una consulta usando SQLAlchemy
    profes = main.getAllTeacher()
    return render_template('Profesores.html', 
                        form = create_form, 
                        profes = profes)

@maestros.route('/agregar-profe', methods = ['GET', 'POST'])
def index():
    create_forms = forms.UserForm(request.form)
    if request.method == 'POST':
        prof = Profesores(nombre = create_forms.nombre.data,
                           apellidos = create_forms.apellidos.data,
                           grupo = create_forms.grupo.data,
                           materia = create_forms.materia.data)
        
        main.saveTeacher(prof.nombre, prof.apellidos, prof.materia, prof.grupo)

        return redirect('profesores')
    
    return render_template('agregar-profe.html', form = create_forms)

@maestros.route('/modificar-profe', methods = ['GET', 'POST'])
def modificarProfe():
    create_forms = forms.UserForm(request.form)
        # Se pretende que muestre una pantalla con los datos del registro
        # Con el fin de que se pueda modificar
    if request.method == 'GET':
    # Obtiene el valor por medio de los parametros en el URL
        id = request.args.get('id')
        prof1 = main.getTeacher(id)
        create_forms.id.data = id
        create_forms.nombre.data = prof1.nombre
        create_forms.apellidos.data = prof1.apellidos
        create_forms.grupo.data = prof1.grupo
        create_forms.materia.data = prof1.materia

    if request.method == 'POST':
        ide = create_forms.id.data
        prof = Profesores(id=ide,
                          nombre=create_forms.nombre.data,
                          apellidos = create_forms.apellidos.data,
                          materia = create_forms.grupo.data,
                          grupo = create_forms.materia.data)

        main.editTeacher(prof.id, prof.nombre, prof.apellidos, prof.grupo, prof.materia)

        return redirect('profesores')

    return render_template("modificar-profe.html", form=create_forms)

@maestros.route("/eliminar-profe", methods = ['GET', 'POST'])
def eliminar():
    create_forms = forms.UserForm(request.form)
    
    # Se pretende que muestre una pantalla con los datos del registro
    # Con el fin de que se pueda modificar
    if request.method == 'GET':
        # Obtiene el valor por medio de los parametros en el URL
        id = request.args.get('id')
        # SELECT * FROM ALUMNOS WHERE id == id
        prof1 = main.getTeacher(id)
        create_forms.id.data = id
        create_forms.nombre.data = prof1.nombre
        create_forms.apellidos.data = prof1.apellidos
        create_forms.grupo.data = prof1.grupo
        create_forms.materia.data = prof1.materia

    if request.method == 'POST':
         id = request.args.get('id')
         main.deleteTeacher(id)
         
         return redirect('profesores')

    return render_template("eliminar-profe.html", form=create_forms, profe = prof1)
