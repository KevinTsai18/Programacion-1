"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#h.Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.

def crearMatriz(n=3):
    filas=6
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
    print("*"*15)


def porcentajeImparesColumna(matriz):
    columna=int(input("ingrese la columna que desea analizar: "))
    impares=0
    for f in range(len(matriz)):
        if matriz[f][columna]%2!=0:
            impares+=1
    print("En la columna", columna, "el", impares*100//len(matriz), "% son impares")


def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    porcentajeImparesColumna(matriz)


main()