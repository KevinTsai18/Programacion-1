"""1.Desarrollar una función para ingresar a través del teclado un número natural.
La función rechazará cualquier ingreso inválido de datos utilizando excepciones
y mostrará la razón exacta del error.
Controlar que se ingrese un número,
que ese número sea entero y que sea mayor que 0.
Devolver el valor ingresado cuando éste sea correcto.
Escribir también un programa que permita probar el correcto funcionamiento de la misma."""


def ingresonronat():
    while True:
        try:
            strnumero=input("Ingrese un número natural: ")
            if not "." in strnumero:
                nro=int(strnumero)
                if nro>0:
                    break
                else:
                    print("El número ingresado no es natural.")
            else:
                print("El número ingresado NO es entero.")
        except ValueError:
            print("Valor no numérico")
    return nro
    


def main():
    nro=ingresonronat()
    print(nro)

main()