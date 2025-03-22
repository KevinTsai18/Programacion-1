"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento
imprimiendo la lista luego de invocar a cada función:
a.Cargar una lista con números al azar de cuatro dígitos.
La cantidad de elementos también será un número al azar de dos dígitos.
b.Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c.Eliminar todas las apariciones de un valor en la lista anterior.
El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
d.Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares.
Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
"""

import random

#Funciones
def cargarlista():
    lista=[]
    cantidad=random.randint(10,99)
    """se obtiene la cantidad de números de la lista
    """
    for i in range(cantidad):
        lista.append(random.randint(1000,9999))
    print(lista)
    return lista
    

def sumarlista(v):
    sumaelem=0
    for i in range(len(v)-1):
        sumaelem=sumaelem+v[i]
    print(sumaelem)

def borrarelemento(num,lista):
    i=0
    while i<len(lista):
        if lista[i]==num:
            del lista[i]
            i=i-1
        i=i+1
    print(lista)
    

def escapicua(lista):
    capicua=True
    for i in range((len(lista)-1)//2):
        if lista[i]!=lista[len(lista)-1-i]:
            capicua=False
    return capicua

#Programa principal
def main():
    listappal=cargarlista()
    sumarlista(listappal)
    elementoaborrar=int(input("Ingrese el número que se desea quitar de la lista"))
    borrarelemento(elementoaborrar,listappal)
    n=int(input())
    if escapicua(listappal):
        print("Es capicua.")
    else:
        print("No es capicua.")

main()