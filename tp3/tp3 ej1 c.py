"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#c.Intercambiar dos filas, cuyos números se reciben como parámetro.

def crearMatriz(cantf=3):
    filas=cantf
    columnas=int(input("Ingrese la cantidad de columnas deseadas: "))
    matriz=[]
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            nro=int(input("Ingrese un número: "))
            matriz[f].append(nro)
    return matriz

def cambiarFilas(matriz):
    fila1=int(input("Ingrese la fila que desea cambiar: "))
    fila2=int(input("Ingrese la fila con la que desea cambiar: "))
    aux=matriz[fila1]
    matriz[fila1]=matriz[fila2]
    matriz[fila2]=aux

def imprimirMatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()


def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    cambiarFilas(matriz)
    imprimirMatriz(matriz)

main()