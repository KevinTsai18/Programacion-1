# 1.Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres.


def contar_rec(numero):
    # Si es negativo le sacamos el signo
    if numero<0:
        numero=-numero
    if numero<10:
        return 1
    else:
        return 1+(contar_rec(numero//10))


def main():
    num=int(input("Ingrese un numero entero: "))
    print(f"La cantidad de digitos que tiene es {contar_rec(num)}")

main()