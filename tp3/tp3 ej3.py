"""3.Desarrollar un programa para rellenar una matriz de N x N
con números enteros al azar comprendidos en el intervalo [0,N**2),
de tal forma que ningún número se repita. Imprimir la matriz por pantalla."""
import random

def crearMatrizCuadrada(cant=3):
    n=cant
    matriz=[]
    lista=[]
    for i in range(n**2):
        lista.append(i)
    print(lista)
    for f in range(n):
        matriz.append([])
        for c in range(n):
            nro=random.randint(0,(n**2)-1)
            while nro not in lista:
                nro=random.randint(0,(n**2)-1)
            matriz[f].append(nro)
            del lista[lista.index(nro)]
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
    matriz=crearMatrizCuadrada()
    imprimirMatriz(matriz)

main()