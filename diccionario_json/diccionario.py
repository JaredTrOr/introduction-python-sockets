import json
import os

path = f'{os.getcwd()}/INTRODUCCION/diccionario_json/ejemplo.json'

with open(path) as archivo:
    data = archivo.read()
    data_diccionario = json.loads(data)
    print(data_diccionario['data'])


diccionario1 = {
    'nombre': 'Pedrito',
    'edad': 20
}

#Transformar diccionario a json
diccionario1_json = json.dumps(diccionario1)

#Transformar json a diccionario
diccionario2 = json.loads(diccionario1_json)