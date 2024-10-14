from datetime import *
import csv   # Para leer los csv de datos
from collections import namedtuple     # Para definir tuplas con nombre

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    entrenos=[]
    with open(fichero,encoding="utf-8") as f:
        lector=csv.reader(f)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime(fechahora)
            ubicacion =str(ubicacion)
            duracion =int(duracion)
            calorias =int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = bool(compartido)
            entreno=Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            entrenos.append(entreno)
    return entrenos

