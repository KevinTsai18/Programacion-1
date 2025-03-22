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
    listaUnicos=[]
    for i in v:
        if i not in listaUnicos:
            listaUnicos.append(i)
    return listaUnicos
        


def main():
    listappal=cargarlista()
    if hayrepetido(listappal):
        print("Hay numeros repetidos.")
    else:
        print("No hay numeros repetidos.")
    print(nuevalista(listappal))



main()