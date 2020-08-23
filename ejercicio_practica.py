'''
MongoDB [Python]
Ejercicio de clase
---------------------------
Autor: Ishef Glatzel
Version: 1.0

Descripcion:
Resolucion del ejercicio planteado en el archivo ejercicio_practica.md
'''

__author__ = "Ishef Glatzel"
__email__ = "Ishefglatzel@gmail.com"
__version__ = "1.0"

from myTinymongoLibrary import connect

import tinymongo as tm
import tinydb

import requests
import json


db_name = 'titulos'


@connect(db_name)
def clear(db=None):
    db.titulo.remove({})


@connect(db_name)
def fill(db=None):
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    dataset = response.json()
    db.titulo.insert_many(dataset)


@connect(db_name)
def title_completed_count(userId, db=None):
    completed_titles = db.titulo.find({"userId": userId, "completed": True}).count()
    print("El usuario {} ha completado {} titulos".format(userId, completed_titles))

if __name__ == "__main__":
  # Borrar DB
  clear()

  # Completar la DB con el JSON request
  fill()

  # Buscar autor
  userId = 5
  title_completed_count(userId)