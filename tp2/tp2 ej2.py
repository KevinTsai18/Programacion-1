"""2.Escribir funciones para:
a.Generar una lista de 50 números aleatorios del 1 al 100.
b.Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido.
La función no debe modificar la lista.
c.Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original,
sin importar el orden. Combinar estas tres funciones en un mismo programa.
"""
import random

#Funciones
def cargarlista():
    lista=[]
    for i in range(20):
        lista.append(random.randint(1,100))
    print(lista)
    return lista
def hayrepetido(v):
    repetido=False
    for i in range(len(v)-2):
        for j in range(i,len(v)-1):
            if v[i]==v[j]:
                repetido=True
    return repetido


def nuevalista(v):
    lista2=v
    i=0
    while i<len(lista2)-1:
        j=i+1
        while j<len(lista2):
            if v[i]==v[j]:
                del v[j]
            j=j+1
        i=i+1
    print(lista2)
        


def main():
    listappal=cargarlista()
    if hayrepetido(listappal):
        print("Hay numeros repetidos.")
    else:
        print("No hay numeros repetidos.")
    nuevalista(listappal)



main()