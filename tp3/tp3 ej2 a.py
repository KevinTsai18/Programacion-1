"""2.Para cada una de las siguientes matrices,
desarrollar una función que la genere y escribir un programa que invoque a
cada una de ellas y muestre por pantalla la matriz obtenida.
El tamaño de las matrices debe establecerse como N x N,
y las funciones deben servir aunque este valor se modifique."""

def funcion2a(cant=4):
    n=cant
    matriz=[]
    i=0
    for f in range(n):
        matriz.append([])
        for c in range(n):
            if f==c:
                matriz[f].append(1+i)
                i=i+2
            else:
                matriz[f].append(0)
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
    matriz=funcion2a()
    imprimirMatriz(matriz)

main()