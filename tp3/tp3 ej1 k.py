"""1.Desarrollar cada una de las siguientes funciones
y escribir un programa que permita verificar su funcionamiento,
imprimiendo la matriz luego de invocar a cada función:"""

#k.Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.

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

def columnaCapicua(matriz):
    listacapicua=[]
    for j in range(len(matriz)):
        esCapicua=True
        i=0
        while i<len(matriz)//2 and esCapicua:
            if matriz[i][j]!=matriz[len(matriz)-1-i][j]:
                esCapicua=False
            else:
                i=i+1
        if esCapicua:
            lista=[]
            for f in range(len(matriz)):
                listacapicua.append(matriz[f][j])
            lista.append(listacapicua)
    print(lista)




def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    columnaCapicua(matriz)

main()