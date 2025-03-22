#7.Escribir una función que reciba una lista como parámetro y
#devuelva True si la lista está ordenada en forma ascendente o False en caso contrario.
#Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False.
#Desarrollar además un programa para verificar el comportamiento de la función. """

def armarLista():
    lista=[]
    elem=input("Ingrese un elemento: ")
    while elem!="basta":
        lista.append(elem)
        elem=input("Ingrese un elemento: ")
    return lista

def esordenada(v):
    orden=True
    for i in range(len(v)-1):
        if v[i]>v[i+1]:
            orden=False
    return orden



def main():
    "Primero armamos la lista"
    
    lista=armarLista()
    print(lista)
    if esordenada(lista):
        print("La lista está ordenada")
    else:
        print("La lista está desordenada")





main()