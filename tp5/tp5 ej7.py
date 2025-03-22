"""7.Escribir un programa que juegue con el usuario a adivinar un número.
El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo.
Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene
que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo,
se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número.
Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y se lo contará como un intento más."""

from random import randint

def main():
    numeroadiv=randint(1,500)
    intentos=1
    while True:
        try:
            nro=float(input("Ingrese un nro: "))
            while nro!=numeroadiv:
                intentos+=1
                if nro>numeroadiv:
                    print("El numero ingresado es MAYOR al secreto.")
                    nro=float(input("Ingrese un nro: "))
                elif nro<numeroadiv:
                    print("El numero ingresado es MENOR al secreto.")
                    nro=float(input("Ingrese un nro: "))
            break
        except ValueError:
            intentos+=1
            print("ERROR. No se ha ingresado un número.")
    print("La cantidad de intentos fue:", intentos)


main()