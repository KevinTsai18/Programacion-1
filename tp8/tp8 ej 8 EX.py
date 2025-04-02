# 8.Definir un conjunto con números enteros entre 0 y 9.
# Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método remove,
# mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
# Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.



def main():
    conj={numero for numero in range(10)}
    print(conj)
    while True:
        try:
            nroelim=int(input("Ingrese un número a eliminar: "))
        except ValueError:
            print("Se ingresó un valor NO entero.")
        else:
            if nroelim==-1:
                break
            try:
                conj.remove(nroelim)
                print("Nuevo conj=",conj)
            except KeyError:
                print("Error. El elemento que se quiere eliminar no se encuentra en el conjunto.")
                


main()