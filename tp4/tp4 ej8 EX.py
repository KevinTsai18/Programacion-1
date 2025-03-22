"""8.Escribir una función que reciba como parámetro
una cadena de caracteres en la que las palabras se encuentran separadas por uno o más espacios.
Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una."""


def ordenarPalabras(cadena):
    #cadena=string.lower()    #Se puede pasar a minuscula
    listapal=cadena.split()   #Sin nada toma todos los espacios para separar
    print(listapal)
    listapal.sort(key=lambda p:p.lower())
    print(" ".join(listapal))



def main():
    frase=input("Ingrese una frase que contenga espacio: ")
    while frase.find(" ")==-1:
        frase=input("Espacio no detectado. Ingrese una frase que contenga espacio: ")
    nuevacad=ordenarPalabras(frase)


main()