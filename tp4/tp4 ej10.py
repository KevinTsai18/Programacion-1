"""10.Escribir un programa que permita ingresar una cadena de caracteres
e imprima un mensaje indicando cuántas letras y cuántos números contiene.
Por ejemplo, si se ingresa "Hola Mundo 123" debe indicar que se ingresaron 9 letras y 3 números."""


def main():
    frase=input("Ingrese una frase: ")
    contnum=0
    contlet=0
    for caracter in range(len(frase)):
        if frase[caracter].isalpha():
            contlet+=1
        elif frase[caracter].isdigit():
            contnum+=1
    print("La cantidad de letras son: ", contlet)
    print("La cantidad de numero son: ", contnum)


main()
