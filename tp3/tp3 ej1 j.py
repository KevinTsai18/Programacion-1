"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.

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


def determSim2(matriz):
    esSim2=True
    i=0
    while i<len(matriz) and esSim2:
        j=len(matriz)-1 #para inicializar cada j con 0
        while j>i and esSim2:  #se recorre la parte inferior para comparar.
            if matriz[j][i]!=matriz[i][j]:
                esSim2=False
            else:
                j-=1
        i+=1
    return esSim2

def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    if determSim2(matriz):
        print("La matriz es simétrica sec.")
    else:
        print("La matriz NO es simétrica sec.")

main()