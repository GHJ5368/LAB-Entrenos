from datetime import datetime
import csv   # Para leer los csv de datos
from collections import namedtuple     # Para definir tuplas con nombre

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    entrenos = []
    with open(fichero,encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            ubicacion =str(ubicacion)
            duracion =int(duracion)
            calorias =int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = bool(compartido)
            entreno=Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            entrenos.append(entreno)
    return entrenos

def tipos_enteros(entrenos):
    '''

    ########### OTRA FORMA ###########

    res = set()
    for entreno in entrenos:
            res.add(entreno.tipo)

    return sorted( res ) ## No hace falta pasar el set a lista

    '''
    
    tipo_entrenos=[]
    for entreno in entrenos:
        if entreno.tipo not in tipo_entrenos:
            tipo_entrenos.append(entreno.tipo)
    
    return sorted(tipo_entrenos)

def entrenos_duracion_superior(entrenos,d):
    res = []
    for entreno in entrenos:
        if entreno.duracion > d:
            res.append(entreno)
    
    return res

def sumar_calorias(entrenos,  f_inicio, f_fin):
    #f_inicio = datetime.strptime(f_inicio, "%Y%m%d")
    #f_fin = datetime.strptime(f_fin, "%Y%m%d")

    res = 0
    
    for entreno in entrenos:
        if f_inicio <=entreno.fechahora <= f_fin  :
            res += entreno.calorias
    
    return res
