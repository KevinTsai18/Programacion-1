"""2.Para cada una de las siguientes matrices,
desarrollar una función que la genere y escribir un programa que invoque a
cada una de ellas y muestre por pantalla la matriz obtenida.
El tamaño de las matrices debe establecerse como N x N,
y las funciones deben servir aunque este valor se modifique."""

def funcion2b(cant=4):
    n=cant
    matriz=[]
    i=n-1
    for f in range(n):
        matriz.append([])
        for c in range(n):
            if c==i:
                matriz[f].append(3**(n-1)//3**(f))
            else:
                matriz[f].append(0)
        i=i-1
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
    matriz=funcion2b()
    imprimirMatriz(matriz)

main()