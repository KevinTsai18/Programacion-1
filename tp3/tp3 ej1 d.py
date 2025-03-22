"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#d.Intercambiar dos columnas dadas, cuyos números se reciben como parámetro. 

def crearMatriz(cantc=3):
    filas=int(input("Ingrese la cantidad de columnas deseadas: "))
    columnas=cantc
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


def cambiarColumnas(matriz):
    columna1=int(input("Ingrese la columna que desea cambiar: "))
    columna2=int(input("Ingrese la columna con la que desea cambiar: "))
    for f in range(len(matriz)):
        aux=matriz[f][columna1]
        matriz[f][columna1]=matriz[f][columna2]
        matriz[f][columna2]=aux
    
        
def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    cambiarColumnas(matriz)
    imprimirMatriz(matriz)

main()