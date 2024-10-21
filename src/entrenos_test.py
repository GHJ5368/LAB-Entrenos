
from entrenos import *

def test_lee_entrenos(fichero):
    #print(f"Estamos probando la carga de datos de Entrenos")
    entrenos = lee_entrenos(fichero)
    #print(f"Tres primeros registros: {entrenos[:3]}")
    #print(f"=======================================")
    #print(f"Tres primeros registros: {entrenos[-3:]}")
    return entrenos

def test_tipos_enteros(entrenos):
    tipos = tipos_enteros(entrenos)
    print(f"Los tiposde entrenos en orden alfabetico son: {tipos}")

def test_entrenos_duracion_superior(entrenos,d):
    res = entrenos_duracion_superior(entrenos,d)
    print(f"Los entrenos superiores a {d} son: {res}")
    
def test_sumar_calorias(entrenos,  f_inicio, f_fin):
    res = sumar_calorias(entrenos,f_inicio, f_fin) 
    print(f"La suma de calorias desde la fecha {f_inicio} hasta la fecha {f_fin} es: {res}")


if __name__ == "__main__":
    fichero = "LAB-Entrenos\data\entrenos.csv"
    entrenos= test_lee_entrenos(fichero)
    #test_tipos_enteros(entrenos)
    #test_entrenos_duracion_superior(entrenos, 10)
    test_sumar_calorias(entrenos, datetime(2020,12,1), datetime.now() )