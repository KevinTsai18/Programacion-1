#10.Escribir una función que sume todos los elementos de una matriz de M x N y devuelva el resultado.


def sumaMatriz_rec(matriz, f=0, c=0):
    if f == len(matriz):
        return 0
    else:
        if c == len(matriz[f]):
            return 0 + sumaMatriz_rec(matriz, f+1)
        else:
            #si corresponde sumo un elemento
                return matriz[f][c] + sumaMatriz_rec(matriz, f, c+1)


def main():
    matriz=[[23,18,25],
            [35,20,21],
            [15,23,4],
            [10,12,32]]
    print(sumaMatriz_rec(matriz))


main()