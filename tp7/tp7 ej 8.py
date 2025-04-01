# 8.Realizar la implementación recursiva del método de selección para ordenar una lista de números enteros.
# Sugerencia: Colocar el elemento más pequeño en la primera posición,
# y luego ordenar el resto de la lista con una llamada recursiva.

def selecc_rec(lista,indice=0):
    if indice!=len(lista):
        #Busco el menor elemento dejandolo en la primera posicion
        posMin=lista.index(min(lista[indice:]))
        #Se podría recorrer con un ciclo for PARA VER SI HAY ALGUN ELEMENTO MENOR
        aux=lista[indice]
        lista[indice]=lista[posMin]
        lista[posMin]=aux
        #vuelvo a llamar con el indice uno mas para ordenar el resto de la lista
        selecc_rec(lista,indice+1)


def main():
    lista=[23,11,35,44,18]
    print(lista)
    selecc_rec(lista)
    print(lista)
    
main()
    