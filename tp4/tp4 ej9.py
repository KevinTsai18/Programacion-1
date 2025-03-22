"""9.Desarrollar una función que devuelva una subcadena con los últimos N caracteres de una cadena dada.
La cadena y el valor de N se pasan como parámetros."""


def ultimosCaracteres(cadena,N):
    nuevacad=cadena[len(cadena)-N:len(cadena)]
    return nuevacad



def main():
    frase=input("Ingrese una frase que contenga espacio: ")
    valor=int(input("Ingrese la cantidad de últimos caracteres que desea: "))
    nuevacad=ultimosCaracteres(frase,valor)
    print(nuevacad)



main()