"""8.Generar dos listas con M y N números al azar entre 1 y 50
y construir una tercera lista cuyos elementos sean el resultado de la intersección de las dos listas dadas.
Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla."""

import random

def armarLista(cantidad):
    "Función carga la cantidad de números entre 1 y 50 al azar recibida como parámetro."
    lista=[]
    for i in range(cantidad):
        lista.append(random.randint(1,50))
    return lista
    

def imprimirLista(lista):
    for numero in lista:
        print(numero, end=" ")
    print(" ")



def interseccion(lista1,lista2):
    """Creamos la tercer lista y vamos agregando los elementos de las 2 listas hasta que no se puedan agregar más de niguna
    de las 2
    
    """
    lista3=[]
    i=0
    while i<len(lista1) and i<len(lista2):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        i=i+1
    """Segun la lista que haya dado todos sus elementos se tiene que ver cual de las dos rellena con lo que quede"""
    
    if i==len(lista1):
        while i<len(lista2):
            lista3.append(lista2[i])
            i=i+1
    else:
        while i<len(lista1):
            lista3.append(lista1[i])
            i=i+1
    return lista3
    
    
    
    
    
    
def main():
    "Armamos con una función 2 listas de M y N números"
    M=random.randint(1,10)
    N=random.randint(1,10)
    listaM=armarLista(M)
    listaN=armarLista(N)
    imprimirLista(listaM)
    imprimirLista(listaN)
    listaMN=interseccion(listaM,listaN)
    imprimirLista(listaMN)

main()