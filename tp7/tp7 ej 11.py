# 11.Desarrollar una función que devuelva el elemento de valor mínimo de una matriz de M x N.


def elemMatrizMenor_rec(matriz,menor,cont=0,f=0,c=0):
    if f==len(matriz):
        return menor
    else:
        cont+=1
        if menor>matriz[f][c]:
            menor=matriz[f][c]
        if c==len(matriz[f])-1:
            return elemMatrizMenor_rec(matriz,menor,cont,f+1,c=0)
        else:
            return elemMatrizMenor_rec(matriz,menor,cont,f,c+1)




def main():
    matriz=[[5,18,25],
            [35,20,21],
            [15,23,26],
            [10,12,8]]
    menor=elemMatrizMenor_rec(matriz,matriz[0][0])
    print(menor)

main()