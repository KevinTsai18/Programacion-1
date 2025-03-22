"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#b.Ordenar en forma ascendente cada una de las filas de la matriz.

def crearMatrizTeclado(n=3):
    matriz=[]
    filas=n
    columnas=n
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(int(input("Ingrese un número: ")))
    return matriz


def imprimirMatrizFormato(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()

def ordenarMatriz(matriz):
    for fila in matriz:
        fila.sort()



def main():
    matriz=crearMatrizTeclado()
    imprimirMatrizFormato(matriz)
    ordenarMatriz(matriz)
    imprimirMatrizFormato(matriz)

main()