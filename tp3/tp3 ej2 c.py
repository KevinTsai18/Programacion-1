

def funcion2c(cant=4):
    n=cant
    i=n
    matriz=[]
    for f in range(n):
        matriz.append([])
        for c in range(1+f):
            matriz[f].append(i)
        while len(matriz[f])<n:
            matriz[f].append(0)
        i=i-1
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
    matriz=funcion2c()
    imprimirMatriz(matriz)

main()