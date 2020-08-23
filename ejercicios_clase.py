#!/usr/bin/env python
'''
MongoDB [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

from myTinymongoLibrary import connect

import json

# Bug: https://github.com/schapman1974/tinymongo/issues/58


db_name = 'secundaria'


@connect(db_name)
def clear(db=None):
    # Eliminar todos los documentos que existan en la coleccion estudiante
    db.estudiante.remove({})


@connect(db_name)
def fill(db=None):
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.
    group = [
        {"name" : "Ishef", "age" : 15, "grade" : 5, "tutor" : "Federico Gonzalez"},
        {"name" : "Francisco", "age" : 14, "grade" : 4, "tutor" : "Celeste Hernandez"},
        {"name" : "Diego", "age" : 13, "grade" : 3, "tutor" : "Juanjo Martinez"},
        {"name" : "Mauricio", "age" : 12, "grade" : 2, "tutor" : "Federico Gonzalez"},
        {"name" : "Maura", "age" : 11, "grade" : 1, "tutor" : "Celeste Hernandez"}
    ]
    db.estudiante.insert_many(group)


@connect(db_name)
def show(db=None):
    print('Comprovemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"

    #conn = TinyMongoClient()
    #db = conn[db_name]

    cursor = db.estudiante.find()
    data = list(cursor)
    json_string = json.dumps(data, indent=4)
    print(json_string)


@connect(db_name)
def find_by_grade(grade, db=None):
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age
    person_data = db.estudiante.find({"grade": grade})
    for data in person_data:
        print(data)
    
    
@connect(db_name)
def insert(student, db=None):
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db
    db.estudiante.insert_one(student)


@connect(db_name)
def count(grade, db=None):
    print('Contar estudiantes')
    # Utilizar la sentencia find + count para contar
    # cuantos estudiantes pertenecen el grado "grade"
    count = db.estudiante.find({"grade": grade}).count()
    print('Hay {} personas que estan cursando el grado {}'.format(count, grade))



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    clear()

    fill()
    show()

    grade = 3
    find_by_grade(grade=grade)

    student = {"name": "Florencia", "age": 16, "grade": 6, "tutor": "Juanjo Martinez"}
    insert(student=student)

    count(grade=grade)
