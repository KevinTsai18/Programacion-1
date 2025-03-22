"""15.Generar una lista con números al azar entre 1 y 100
y crear una nueva lista con los elementos de la primera que sean impares.
El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla. """

import random

def armarLista(cant=10):
    lista=[]
    for i in range(cant):
        lista.append(random.randint(1,100))
    return lista



def main():
    listappal=armarLista()
    print(listappal)
    listaimpar=[elem for elem in listappal if elem%2!=0]
    print(listaimpar)
    
main()