"""9.Escribir una función que reciba una lista de números enteros como parámetro y la normalice,
es decir que todos sus elementos deben sumar 1.0,
respetando las proporciones relativas que cada elemento tiene en la lista original.
Desarrollar también un programa que permita verificar el comportamiento de la función.
Por ejemplo, normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
import random
#LA SUMA DE LOS ELEMENTOS DESPUES SE USA PARA DIVIDIR LOS ELEMENTOS POR SEPARADO Y DA LA NUEVA LISTA
def armarLista():
    cantidad=random.randint(5,12)
    lista=[]
    for i in range(cantidad):
        lista.append(random.randint(1,20))
    return lista
    
def imprimirLista(v):
    for elem in v:
        print(elem, end=" ")
    print()

def normalizar(lista):
    suma=0
    for elem in lista:
        suma=suma+elem
    print(suma)
    for i in range(len(lista)):
        lista[i]=lista[i]/suma
    return lista

def main():
    "Armamos una lista con la función"
    lista=armarLista()
    imprimirLista(lista)
    normalizar(lista)
    print(lista)




main()

