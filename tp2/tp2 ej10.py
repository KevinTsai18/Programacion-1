#10.Generar una lista con números al azar entre 0 y 100,
#donde su cantidad de elementos será un número par también obtenido al azar entre 10 y 50.
#Luego se solicita partir la lista por la mitad a través de la técnica de las rebanadas,
#creando dos nuevas listas. Imprimir las tres listas por pantalla.

import random

def cantidadPar():
    cantidad=random.randint(5,25) * 2
    "ASÍ SEGURO DA PAR"
    return cantidad

def armarLista(cant):
    lista=[]
    for i in range(cant):
        lista.append(random.randint(0,100))
    return lista

def imprimirLista(lista):
    for numero in lista:
        print(numero, end=" ")
    print()


def main():
    cantlista=cantidadPar()
    listappal=armarLista(cantlista)
    imprimirLista(listappal)
    primermitad=listappal[:len(listappal)//2]
    imprimirLista(primermitad)
    segundamitad=listappal[len(listappal)//2:]
    imprimirLista(segundamitad)


main()