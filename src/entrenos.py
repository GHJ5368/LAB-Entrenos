from datetime import *
import csv   # Para leer los csv de datos
from collections import namedtuple     # Para definir tuplas con nombre

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    entrenos=[]
    with open(fichero,encoding="utf-8") as f:
        lector=csv.reader(f)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = int

