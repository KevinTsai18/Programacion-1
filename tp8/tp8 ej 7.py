# 7.Ingresar una frase desde el teclado y eliminar las palabras repetidas,
# dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.
# La eliminación de las palabras duplicadas debe realizarse a través de un conjunto.
# Frase: If you run into a wall and pretend it does not exist, you will never make any progress. The wall will never change, so you are the one who has to change



def main():
    frase=input("Ingrese una frase: ")
    lista=frase.split()
    print(lista)
    conjunto=set(lista)
    print(conjunto)
    listafinal=list(conjunto)
    print(listafinal)
    #listafinal=sorted(listafinal, key=lambda palabra:len(palabra))
    listafinal.sort(key=lambda palabra:len(palabra))
    #SORT= METODO QUE ORDENA LISTA
    #SORTED= FUNCION QUE CREA OTRA VARIABLE
    print(listafinal)


main()
    
    
    