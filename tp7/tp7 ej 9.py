# 9.Realizar una función recursiva para imprimir una matriz de M x N.

def imprimirMatriz(matriz):
    if len(matriz)!=0:
        # print(matriz[0])
        #Ahora para darle formato...
        #for i in range(len(matriz[0])):
            #print("%3d" %matriz[0][i], end="")
        #print()
        #...Y para no usar ciclos y que sea 100% recursivo...
        
        imprimirMatriz(matriz[1:])




def main():
    matriz=[[23,18,25],
            [35,20,21],
            [15,23,4],
            [10,12,32]]
    imprimirMatriz(matriz)

main()