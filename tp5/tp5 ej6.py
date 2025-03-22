"""6.El método index permite buscar un elemento dentro de una lista,
devolviendo la posición que éste ocupa. Sin embargo,
si el elemento no pertenece a la lista se produce una excepción de tipo ValueError.
Desarrollar un programa que cargue una lista con números enteros ingresados a través del teclado
(terminando con -1) y permita que el usuario ingrese el valor de algunos elementos
para visualizar la posición que ocupan, utilizando el método index.
Si el número no pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar.
Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda. """



def armarLista():
    lista=[]
    n=int(input("Ingrese un número para agregar a la lista: "))
    while n!=-1:
        lista.append(n)
        n=int(input("Ingrese un número para agregar a la lista: "))
    return lista

def revisarLista(lista):
    cont=0
    while True:
        try:
            elem=int(input("Ingrese el elemento que desea ver si está en la lista: "))
            poselem=lista.index(elem)
            print("El elemento", elem, "se encuentra en la posición", poselem)
            break
        except ValueError:
            print("Error. El elemento no se encuentra en la lista.")
            cont+=1
            if cont==3:
                print("Proceso abortado.")
                break
            


def main():
    lista=armarLista()
    revisarLista(lista)

main()