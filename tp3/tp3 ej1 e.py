"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#e.Intercambiar una fila por una columna, cuyos números se reciben como parámetro.

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

def cambiarFilaColumna(matriz):
    fila=int(input("Ingrese la fila que desea cambiar: "))
    columna=int(input("Ingrese la columna que desea cambiar: "))
    aux=matriz[fila].copy()
    for f in range(len(matriz)):
        matriz[fila][f]=matriz[f][columna]
    for f in range(len(matriz)):
        matriz[f][columna]=aux[f]


def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    cambiarFilaColumna(matriz)
    imprimirMatriz(matriz)

main()