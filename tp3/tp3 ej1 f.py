"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)

def crearMatriz(n=3):
    filas=n
    columnas=n
    matriz=[]
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            nro=int(input("Ingrese un número: "))
            matriz[f].append(nro)
    return matriz

def imprimirMatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()
    print("*"*10)

def trasponer(matriz):
    i=0
    for f in range(len(matriz)):
        for c in range(i,len(matriz[f])):
            aux=matriz[f][c]
            matriz[f][c]=matriz[c][f]
            matriz[c][f]=aux
        i=i+1

def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    trasponer(matriz)
    imprimirMatriz(matriz)


main()