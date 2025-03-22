"""6.Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
"""




def main():
    lista1=["somebody","once","once","told","me","the","world","once"]
    lista2=["once","told","me"]
    print(lista1)
    print(lista2)
    i=0
    for j in range(len(lista2)):
        while i<len(lista1):
            if lista2[j]==lista1[i]:
                del lista1[i]
                i=i-1
            i=i+1
        i=0
    print(lista1)
                

main()