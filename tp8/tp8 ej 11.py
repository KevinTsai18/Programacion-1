# 11.Desarrollar una función eliminarclaves() que reciba como parámetros
# un diccionario y una lista de claves. La función debe eliminar del diccionario
# todas las claves contenidas en la lista, devolviendo el diccionario
# modificado y un valor de verdad que indique si la operación fue exitosa.
# Desarrollar también un programa para verificar su comportamiento.


def eliminarClaves(dicc,listaclaves):
    op=True
    while op:
        try:
            for clave in listaclaves:
                del dicc[clave]
            break
        except KeyError:
            op=False
        finally:
            return op,dicc


def main():
    dicc={"rojo":[255,0,0],
          "verde":[0.255,0],
          "azul":[0,0,255]
          }
    lista=("amarillo",)
    resultado,dicc=eliminarClaves(dicc,lista)
    print(dicc)
    if resultado:
        print("Se eliminaron las claves correctamente.")
    else:
        print("Hubo claves que no se pudieron eliminar.")

main()
    