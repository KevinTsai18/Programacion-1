def funcion2f(cant=4):
    n=cant
    matriz=[]
    elem=1
    cont=1
    for f in range(n):
        matriz.append([])
        for c in range(n):
            if c<cont:
                matriz[f].append(elem)
                elem=elem+1
            else:
                matriz[f].append(0)
        cont=cont+1
        matriz[f].reverse()
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
    matriz=funcion2f()
    imprimirMatriz(matriz)

main()