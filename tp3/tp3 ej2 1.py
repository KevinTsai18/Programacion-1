#2.Para cada una de las siguientes matrices,
#desarrollar una función que la genere y escribir un programa
#que invoque a cada una de ellas y muestre por pantalla la matriz obtenida.
#El tamaño de las matrices debe establecerse como N x N, y las funciones deben servir aunque este valor se modifique.

# DEBE SERVIR PARA CUALQUIER N




def funcion2a():
    n=4
    i=0
    matriz=[]
    for f in range(n):
        matriz.append([None]*n)
    for i in range(n):
        matriz[i]=[[2*i+1 if i==j else 0 for j in range(n)] for i in range(n)]
    print(matriz)

def main():
    funcion2a()

main()