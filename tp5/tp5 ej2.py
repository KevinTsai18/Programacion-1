"""2.Realizar una función que reciba como parámetros
dos cadenas de caracteres conteniendo números reales,
sume ambos valores y devuelva el resultado como un número real.
Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""


def sumacadnro(cad1,cad2):
    try:
        nro1=float(cad1)
        nro2=float(cad2)
        suma=nro1+nro2
    except ValueError:
        print("Error. La cadena igresada no contiene números reales.")
        suma=-1
    return suma
    

def main():
    cadena1=input("Ingrese un número real: ")
    cadena2=input("Ingrese otro número real: ")
    suma=sumacadnro(cadena1,cadena2)
    if suma==-1:
        print("uno de los valores ingresados no es numérico")
    else:
        print("El resultado de la suma fue", suma)


main()