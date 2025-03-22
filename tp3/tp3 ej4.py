"""4.2048 es un juego que se desarrolla en una cuadrícula de 4 x 4,
donde en cada celda hay una baldosa con un número 2 o 4 generados al azar.
Se utilizan las teclas de dirección para mover las baldosas:
4 (izquierda), 6 (derecha), 8 (arriba) y 2 (abajo).
Estas baldosas se deslizan sobre el tablero en el sentido indicado por la tecla presionada.
Si dos baldosas con el mismo número "colisionan" durante un movimiento,
se combinarán en una nueva baldosa cuyo valor será la suma de los valores de las dos baldosas originales,
es decir que si dos baldosas con el número 4 colisionan, éstas se combinarán en una baldosa con el número 8.
Sin embargo la baldosa resultante no podrá combinarse con otra en esa misma jugada. 
Las jugadas se realizan ingresando la fila y columna de la baldosa a desplazar
y la dirección en que se mueve.
En el espacio vacío dejado por la baldosa desplazada aparecerá una nueva baldosa conteniendo un número 2 o 4,
generado al azar. El juego finaliza cuando se obtiene una baldosa con el número 2048.
Escribir un programa que permita jugarlo e informe la cantidad de jugadas realizadas hasta finalizar."""

from random import randint

def crearMatriz():
    n=4
    matriz=[[randint(1,2)*2 for c in range(n)] for f in range(n)]
    return matriz


def imprimirMatriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            print("%4d" %matriz[f][c], end=" ")
        print()
        print()


def juego(matriz):
    n=4
    direcpos=[2,4,6,8]
    jugadas=0
    while max(matriz[0])!=16 and max(matriz[1])!=16 and max(matriz[2])!=16 and max(matriz[3])!=16:
        fila=int(input("Ingrese la fila de la casilla a mover: "))
        columna=int(input("Ingrese la columna de la casilla a mover: "))
        direccion=int(input("Ingrese la dirección para mover la celda: "))
        while direccion not in direcpos:
            direccion=int(input("Dirección inválida. Seleccione otra: "))
        if direccion==2:
            if fila+1<n:
                if matriz[fila][columna]==matriz[fila+1][columna]:
                    matriz[fila+1][columna]=matriz[fila+1][columna]*2
                    matriz[fila][columna]=randint(1,2)*2
                    jugadas+=1
        elif direccion==8:
            if fila-1>=0:
                if matriz[fila][columna]==matriz[fila-1][columna]:
                    matriz[fila-1][columna]=matriz[fila-1][columna]*2
                    matriz[fila][columna]=randint(1,2)*2
                    jugadas+=1
        elif direccion==4:
            if columna-1>=0:
                if matriz[fila][columna]==matriz[fila][columna-1]:
                    matriz[fila][columna-1]=matriz[fila][columna-1]*2
                    matriz[fila][columna]=randint(1,2)*2
                    jugadas+=1
        elif direccion==6:
            if columna+1<n:
                if matriz[fila][columna]==matriz[fila][columna+1]:
                    matriz[fila][columna+1]=matriz[fila][columna+1]*2
                    matriz[fila][columna]=randint(1,2)*2
                    jugadas+=1
        imprimirMatriz(matriz)
    return jugadas
            

def main():
    matriz=crearMatriz()
    imprimirMatriz(matriz)
    jugadas=juego(matriz)
    print("la cantidad de jugadas fueron: ", jugadas)

main()