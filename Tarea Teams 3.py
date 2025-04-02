#3)Desarrollar un programa que resuelva la siguiente situación problemática (no olvidarse de modularizar):
#“Un productor de naranjas desea contabilizar sus cajones de naranjas
#según el peso para poder cargar luego los camiones de reparto.
#En un cajón entran 100 naranjas con un peso entre 200 y 300 gramos cada una,
#si la naranja supera o es menor al rango del peso indicado, se clasifica para procesar como jugo.
#Se necesita un programa que al ingresar la cantidad de naranjas producidas,
#le  informe  cuántos  cajones  se llenan, el  peso  de  cada cajón
#(para  luego  cargar  los  camiones  de  reparto),
#cuántas  naranjas  son  para  jugo y el peso de las naranjas sobrantes
#que se debe considerar para el siguiente reparto.
#”Simular el peso de cada naranja con un número al azar entre 150 y 350.
"""Mostrar como están creados cada cajón indicando además el peso de cada cajón
y su peso total mostrando primero el cajón de mayor peso al menor peso.
(Esto se puede guardar en una matriz donde cada fila representa un cajón y cada columna una naranja).
Mostrar las naranjas sobrantes y las naranjas para jugo ordenadas por peso de menor a mayor. """



import random

def armarLista(cantidad):
    lista=[]
    for i in range(cantidad):
        lista.append(random.randint(150,350))
    return lista

def separarcajones(lista):
    cantcajon=0
    while len(lista)>=100:
        cajon=[]
        i=0
        while i<10:
            cajon.append(lista[0])
            del lista[0]
            i=i+1
        cantcajon=cantcajon+1
        calcularPeso(cajon,cantcajon)
    return cantcajon
    

def calcularPeso(cajon,numero):
    peso=sum(cajon)
    print("El cajon", numero, "pesa", peso)
    
        

def main():
    cantidad=int(input("Ingrese la cantidad de naranjas producidas: "))
    lista=armarLista(cantidad)
    print(lista)
    listacajon=[peso for peso in lista if peso>=200 and peso<=300]
    print(listacajon)
    listajugo=[peso for peso in lista if peso<200 or peso>300]
    print(listajugo)
    print(len(listajugo), "naranjas son para jugo.")
    cajonesllenos=separarcajones(listacajon)
    print(listacajon)
    print("Se llenan", cajonesllenos, "cajones")
    print("Sobran", sum(listacajon), "gramos en naranjas.")


main()