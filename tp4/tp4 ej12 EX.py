"""12.Desarrollar una función para reemplazar todas las apariciones de una palabra
por otra en una cadena de caracteres y devolver la cadena obtenida
y un entero con la cantidad de reemplazos realizados.
Escribir también un programa para verificar el comportamiento de la función. """


def reemplazar(cadena):
    pal=input("Ingrese la palabra a reemplazar: ")
    reemp=input("Ingrese su reemplazo: ")
    lista=cadena.split(" ")
    cont=cadena.count(pal)
    cadena=cadena.replace(pal,reemp)
    return (cadena,cont)



def main():
    frase=input("ingrese una cadena: ")
    frase,cantreemp=reemplazar(frase)
    print(frase)
    print("La cantidad de reemplazos fueron", cantreemp)


main()