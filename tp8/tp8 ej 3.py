# 3. Desarrollar un programa que utilice una función que reciba como parámetro
# una cadena de caracteres conteniendo una dirección de correo electrónico
# y devuelva una tupla con las distintas partes que componen dicha dirección.
# Ejemplo: alguien@uade.edu.ar -> (alguien, uade, edu, ar).


def tuplaDireccion(mail):
    partes=()
    parte1=mail[:mail.index("@")]
    partes+=(parte1,)
    parte2=mail[mail.index("@")+1:].split(".")
    for cad in parte2:
        partes+=(cad,)
    return partes




def main():
    mail=input("Ingrese una dirección de correo electrónico: ")
    partes=tuplaDireccion(mail)
    print(partes)


main()