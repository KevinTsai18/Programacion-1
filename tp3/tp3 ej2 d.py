def funcion2d(cant=4):
    n=cant
    matriz=[]
    for f in range(n):
        matriz.append([])
        for c in range(n):
            matriz[f].append(2**(n-f-1))
    return matriz


def imprimirMatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()
    print("*"*15)



def main():
    matriz=funcion2d()
    imprimirMatriz(matriz)

main()