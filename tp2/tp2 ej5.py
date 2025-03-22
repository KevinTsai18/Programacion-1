"""5.Escribir un programa que calcule la suma acumulada a partir de una lista de números.
El programa debe generar una nueva lista donde el primer elemento es el mismo de la lista original,
el segundo elemento es la suma del primero más el segundo,
el tercer elemento es la suma del primero más el segundo más el tercero y así sucesivamente.
Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6].
"""

import random

def main():
    lista1=[]
    for i in range(10):
        lista1.append(random.randint(1,9))
    print(lista1)
    lista2=[lista1[0]]
    suma=lista1[0]
    for j in range(1,len(lista1)-1):
        suma=suma+lista1[j]
        lista2.append(suma)
    print(lista2)


main()
