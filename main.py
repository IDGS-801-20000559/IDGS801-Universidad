from db import get_connection
from models import Profesores;

# Consulta de todos los profesores
def getAllTeacher():
    listaProfes = []
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            #Sirve para ejecutar un stored procedure
            curso.execute('call consulta_profesores()')
            resultset = curso.fetchall()
            for row in resultset:
                profe = Profesores(id=row[0], 
                                   nombre=row[1],
                                   apellidos = row[2],
                                   materia = row[3],
                                   grupo = row[4])

                listaProfes.append(profe)
                
        connection.close()
               
    except Exception as ex:
        print(ex)

    return listaProfes

# Consulta por id
def getTeacher(id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            #Sirve para ejecutar un stored procedure
            curso.execute('call consulta_profesor(%s)', id)
            resultset = curso.fetchall()
            row = resultset[0]
            profe = Profesores()
            profe.id = row[0]
            profe.nombre = row[1]
            profe.apellidos = row[2]
            profe.materia = row[3]
            profe.grupo = row[4]
        connection.close()
        return profe       
    except Exception as ex:
        print(ex)

# Guardar un nuevo profesor
def saveTeacher(nombreN, apellidosN, materiaN, grupoN):
    response = ""
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            #Sirve para ejecutar un stored procedure
            params = (nombreN, apellidosN, materiaN, grupoN)
            curso.callproc('agrega_profesor', params)
            connection.commit()
            resultset = curso.fetchall()
            response = resultset
            print("Datos insertados correctamente.")
        connection.close()
               
    except Exception as ex:
        print(ex)
    return response

# Modificar un profesor ya existente
def editTeacher(idM, nombreM, apellidosM, materiaM, grupoM):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            #Sirve para ejecutar un stored procedure
            query = 'call modificar_profesor(%s, %s,%s,%s, %s)'
            params = (idM,nombreM, apellidosM, materiaM, grupoM)
            print(query % params) # Imprimir la consulta formateada
            curso.execute(query, params)
            connection.commit()
            resultset = curso.fetchall()

            for row in resultset:
                print(row)

        print("Datos modificados correctamente.")
        connection.close()
    
    except Exception as ex:
        print(ex)

# Eliminar un profesor
def deleteTeacher(ide):
    response = ""
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            #Sirve para ejecutar un stored procedure
            query = 'call eliminar_profesor(%s)'
            params = (ide)
            print(query % params) # Imprimir la consulta formateada
            curso.execute(query, params)
            connection.commit()
            resultset = curso.fetchall()
            response = resultset
        print("Registro eliminado correctamente.")
        connection.close()
    except Exception as ex:
        print(ex)
    return response

"""

#Consulta de todos  los alumnos
try:
    connection = get_connection()
    with connection.cursor() as curso:
        #Sirve para ejecutar un stored procedure
        curso.execute('call consulta_alumnos()')

        resultset = curso.fetchall()

        for row in resultset:
            print(row)

    connection.close()
    
except Exception as ex:
    print('Error '+ex)

# Consulta de solo un alumno
try:
    connection = get_connection()
    with connection.cursor() as curso:
        #Sirve para ejecutar un stored procedure
        curso.execute('call consulta_alumno(3)')

        resultset = curso.fetchall()

        for row in resultset:
            print(row)

    connection.close()
except Exception as ex:
    print('Error '+ex)

try:
    connection = get_connection()
    with connection.cursor() as curso:
        #Sirve para ejecutar un stored procedure
        curso.execute('call agrega_alumno(%s, %s, %s)', ('valor1', 'valor2', 'valor3'))

        resultset = curso.fetchall()

        for row in resultset:
            print(row)

    connection.close()
    
except Exception as ex:
    print('Error '+ex)
"""