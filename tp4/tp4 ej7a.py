"""7.Escribir una función para eliminar una subcadena de una cadena de caracteres,
a partir de una posición y cantidad de caracteres dadas,
devolviendo la cadena resultante.
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a.Utilizando rebanadas
b.Sin utilizar rebanadas"""


def subcadena(cadena):
    pos=int(input("Ingrese a partir de qué posición desea tomar: "))
    cant=int(input("Ingrese la cantidad de caracteres a tomar: "))
    while pos+cant>len(cadena):
        cant=int(input("Cantidad inválida. Ingrese la cantidad de caracteres a tomar: "))
    nuevacad=cadena[:pos]+cadena[pos+cant:]
    return nuevacad



def main():
    frase=input("Ingrese una frase: ")
    nuevacad=subcadena(frase)
    print(nuevacad)
    
main()