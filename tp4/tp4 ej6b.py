"""6.Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada.
Devolver la subcadena como valor de retorno.
Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena "El número de teléfono es 4356-7890"
extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890".
Escribir una función para cada uno de los siguientes casos:
b.Sin utilizar rebanadas"""


def subcadena(cadena):
    pos=int(input("Ingrese a partir de qué posición desea tomar: "))
    cant=int(input("Ingrese la cantidad de caracteres a tomar: "))
    while pos+cant>len(cadena):
        cant=int(input("Cantidad inválida. Ingrese la cantidad de caracteres a tomar: "))
    nuevacad=""
    for i in range(pos,pos+cant):
        nuevacad=nuevacad+cadena[i]
    return nuevacad



def main():
    frase=input("Ingrese una frase: ")
    nuevacad=subcadena(frase)
    print(nuevacad)
    
main()