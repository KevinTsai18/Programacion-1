"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#g.Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.

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
    print("*"*15)

def calcularPromedio(matriz):
    for f in range(len(matriz)):
        print("El promedio de la fila", f, "es", sum(matriz[f])//len(matriz[f]))

def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    calcularPromedio(matriz)

main()