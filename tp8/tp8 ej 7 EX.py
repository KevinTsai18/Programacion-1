# 7.Ingresar una frase desde el teclado y eliminar las palabras repetidas,
# dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.
# La eliminación de las palabras duplicadas debe realizarse a través de un conjunto.


def operaCad(cad):
    cadList=cad.lower().split()
    ListConj=set(cadList)
    ConjList=list(ListConj)
    ConjList.sort(key=len)
    # Ordena por longitud. Para hacerlo al revés, cadena.sort(key=len,reverse=True)
    return ConjList





def main():
    frase=input("Ingrese una frase: ")
    print("Respuesta: ", operaCad(frase))


main()