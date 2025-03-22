def funcion2e(cant=4):
    n=cant
    matriz=[]
    elem=1
    impar=True
    for f in range(n):
        matriz.append([])
        for c in range(n):
            if impar==True:
                matriz[f].append(0)
                impar=False
            else:
                matriz[f].append(elem)
                impar=True
                elem+=1
        if f%2==0:
            impar=False
        else:
            impar=True
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
    matriz=funcion2e()
    imprimirMatriz(matriz)

main()