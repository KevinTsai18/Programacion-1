#2)Desarrollar la función y el programa detallados:

#a)Desarrollar una función lambda que indique si un número es par o impar.

#b)Realizar un programa que solicite por teclado números al azar entre 1 y 50.
#Dichos números deben ser separados en 2 listas, una para los pares y otra para los impares.
#Se finaliza la carga de valores al ingresar el cero, los valores deben ir siendo agregados
#a una lista o a la otra al momento de ser ingresados, utilizando la función del inciso a).

import random

esPar=lambda n:True if n%2==0 else False

def main():
    listapar=[]
    listaimpar=[]
    n=int(input("Ingrese un número del 1 al 50 al azar: "))
    while n!=0:
        while n>50 or n<0:
            n=int(input("Número inválido. Ingrese otro número: "))
        if esPar(n):
            listapar.append(n)
        else:
            listaimpar.append(n)
        n=int(input("Ingrese un número del 1 al 50 al azar: "))
    print(listapar)
    print(listaimpar)

main()