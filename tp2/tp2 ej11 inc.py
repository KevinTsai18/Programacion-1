#11.Intercalar los elementos de una lista entre los elementos de otra.
#La intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas
#y no se creará una lista nueva sino que se modificará la primera.
#Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

import random

def armarLista():
    cant=random.randint(3,8)
    lista=[]
    for i in range(cant):
        lista.append(random.randint(0,10))
    return lista

def imprimirLista(v):
    for elem in v:
        print(elem, end=" ")
    print()

def intercalar(lista1,lista2):
    for i in range(len(lista2)-1,-1,-1):
        lista1[i+1:i+1]=[lista2[i]]

def main():
    listaA=armarLista()
    listaB=armarLista()
    if len(listaA)>len(listaB):
        lista1=listaA
        lista2=listaB
    else:
        lista1=listaB
        lista2=listaA
    imprimirLista(lista1)
    imprimirLista(lista2)
    intercalar(lista1,lista2)
    print(lista1)


main()