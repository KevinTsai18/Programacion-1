"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#i. Determinar si la matriz es simétrica con respecto a su diagonal principal.

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


def determSim(matriz):
    esSim=True
    i=0
    while i<len(matriz) and esSim:
        j=0 #para inicializar cada j con 0
        while j<i and esSim:  #se recorre la parte inferior para comparar.
            if matriz[i][j]!=matriz[j][i]:
                esSim=False
            else:
                j+=1
        i+=1
    return esSim

def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    if determSim(matriz):
        print("La matriz es simétrica.")
    else:
        print("La matriz NO es simétrica.")


main()