"""5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo."""

#Conviene controlar que es numero en otra funcion


import math

def raizcuadrada():
    while True:
        try:
            nro=int(input("Ingrese un número: "))
            nro=math.sqrt(nro)
            #if nro>=0:    #El resultado siempre es positivo
            break
        except ValueError:
            print("La raíz cuadrada no permite números negativos")
    return nro
    


def main():
    nro=raizcuadrada()
    print(nro)

main()