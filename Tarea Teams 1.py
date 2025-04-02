#1)Desarrollar la función y el programa detallados:

#a)Desarrollar una función para crear una lista con N elementos al azar.
#Se debe recibir por parámetro en valor N y el rango en el que puede estar cado uno de esos elementos(desde y hasta).
#En caso de no recibir N por parámetro, se debe crear la lista con 20 elementos;
#y en caso de no recibir el rango, se deben tomar los valores de 1 a 100.

#b)Utilizando  la  función  anterior, realizar un programa que cree una lista con N elementos al azar entre 1 y 100.
#Mostrar  el  promedio de la misma y aquellos elementos que sean mayores al promedio,
#ordenados de menor a mayor. Se requiere utilizar la función sum para calcular el promedio,
#y la creación de la lista de los elementos que superan el promedio se realice por comprensión.

import random

def armarLista(N=5,rango1=1,rango2=100):
    lista=[]
    for i in range(N):
        lista.append(random.randint(rango1,rango2))
    return lista


def main():
    lista=armarLista()
    print(lista)
    print("El promedio de la lista es", sum(lista)//len(lista))
    listamayores=[num for num in lista if num>sum(lista)//len(lista)]
    print(listamayores)

main()
