"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""
#a.Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado.


def crearMatrizTeclado(n=3):
    """retorna matriz
    """
    matriz=[]
    filas=n
    columnas=n
    for f in range(filas):
        matriz.append([]) #agrego una lista que representa una fila de la matriz
        for c in range(columnas):
            nro=int(input("Ingrese un número: "))
            matriz[f].append(nro)
    return matriz

def imprimirConOperadorIn(matriz):
    for fila in matriz:
        print(fila)

def imprimirMatrizFormato(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()

def main():
    m=crearMatrizTeclado()
    imprimirConOperadorIn(m)
    imprimirMatrizFormato(m)
    
main()