"""8.Escribir una función que reciba como parámetro
una cadena de caracteres en la que las palabras se encuentran separadas por uno o más espacios.
Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una."""


def ordenarPalabras(cadena):
    #cadena=string.lower()    #Se puede pasar a minuscula
    listapal=cadena.split(" ")
    print(listapal)
    #cadena=cadena.sort()
    if len(listapal)==1:
        nuevacad=cadena
    for i in range(len(listapal)-1):
        for j in range(i,len(listapal)):
            if listapal[i]>listapal[j]:
                aux=listapal[j]
                listapal[j]=listapal[i]
                listapal[i]=aux
    print(listapal)



def main():
    frase=input("Ingrese una frase que contenga espacio: ")
    while frase.find(" ")==-1:
        frase=input("Espacio no detectado. Ingrese una frase que contenga espacio: ")
    nuevacad=ordenarPalabras(frase)


main()