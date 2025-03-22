"""1.Desarrollar una función para ingresar a través del teclado un número natural.
La función rechazará cualquier ingreso inválido de datos utilizando excepciones
y mostrará la razón exacta del error.
Controlar que se ingrese un número,
que ese número sea entero y que sea mayor que 0.
Devolver el valor ingresado cuando éste sea correcto.
Escribir también un programa que permita probar el correcto funcionamiento de la misma."""


def ingresonronat():
    try:
        numero=int(input("Ingrese un número natural: "))
        while numero<0:
            numero=int(input("Número menor que 0. Ingrese un número natural: "))
        return numero
    except ValueError:
        print("Error. No se ingresó un número entero.")
    


def main():
    nro=ingresonronat()
    if nro!=None:
        print(nro)

main()