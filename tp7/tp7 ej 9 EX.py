# 9.Realizar una función recursiva para imprimir una matriz de M x N.

def imprimirMatriz(matriz,f=0,c=0):
    if f==len(matriz):
        print()
    else:
        print("%3d" %matriz[f][c], end="")
        if c==len(matriz[f])-1:
            print()
            imprimirMatriz(matriz,f+1,c=0)
        else:
            imprimirMatriz(matriz,f,c+1)




def main():
    matriz=[[23,18,25],
            [35,20,21],
            [15,23,4],
            [10,12,32]]
    imprimirMatriz(matriz)

main()