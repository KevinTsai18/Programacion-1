def funcion2h(cant=5):
    n=cant
    matriz=[[None]*n for i in range(n)]
    print(matriz)
    cont=0
    a=0
    b=cont
    elem=1
    while elem<=n**2:
        while a<=cont and a<n:
            b=cont-a
            while b>=n:
                a=a+1
                b=cont-a
            matriz[a][b]=elem
            elem=elem+1
            a=a+1
            b=b-1
        cont=cont+1
        a=0
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
    matriz=funcion2h()
    print(matriz)
    imprimirMatriz(matriz)

main()