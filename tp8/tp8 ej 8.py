# 8.Definir un conjunto con números enteros entre 0 y 9.
# Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove,
# mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
# Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.

# from random import randint


# def generarConjunto():
#     conjunto=[]
#     for i in range(randint(1,9)):
#         conjunto.append(randint(1,9))
#     conjunto=set(conjunto)
#     return conjunto



def main():
    conj={numero for numero in range(10)}
    print(conj)
    while True:
        try:
            nroelim=int(input("Ingrese un número a eliminar: "))
            if nroelim==-1:
                break
            conj.remove(nroelim)
            print(conj)
        except KeyError:
            print("Error. El elemento que se quiere eliminar no se encuentra en el conjunto.")
        except ValueError:
            print("Se ingresó un valor NO entero.")


main()