def funcion2g(cant=6):
    n=cant
    matriz=[]
    elem=1
    fila=0
    columna=0
    inverso=False
    for f in range(n):
        matriz.append([])
        for c in range(n):
            matriz[f].append(None)
    while elem<=n**2:
        if not inverso:
            for c in range(n):
                if matriz[fila][c]==None:
                    matriz[fila][c]=elem
                    elem=elem+1
                    columna=c
            for f in range(n):
                if matriz[f][columna]==None:
                    matriz[f][columna]=elem
                    elem=elem+1
                    fila=f
            inverso=True
        else:
            for c in range(-1,-n-1,-1):
                if matriz[fila][c]==None:
                    matriz[fila][c]=elem
                    elem=elem+1
                    columna=columna-1
            for f in range(-1,-n-1,-1):
                if matriz[f][columna]==None:
                    matriz[f][columna]=elem
                    elem=elem+1
                    fila=fila-1
            inverso=False
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
    matriz=funcion2g()
    print(matriz)
    imprimirMatriz(matriz)

main()