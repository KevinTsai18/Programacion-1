"""1.Desarrollar una función que determine si una cadena de caracteres es capicúa,
sin utilizar cadenas auxiliares.
Escribir además un programa que permita verificar su funcionamiento."""

def esCapicua(cad):
    capicua=True
    i=0
    while i<len(cad)//2 and capicua==True:
        if cad[i]!=cad[len(cad)-1-i]:
            capicua=False
        i=i+1
    return capicua


def main():
    cadena=input("Ingrese una cadena de caracteres: ")
    if esCapicua(cadena):
        print("La cadena es capicua.")
    else:
        print("La cadena NO es capicua.")


main()