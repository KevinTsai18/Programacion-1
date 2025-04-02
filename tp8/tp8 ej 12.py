# 12.Crear una función contarvocales(), que reciba una palabra
# y cuente cuántas letras "a" contiene, cuántas "e", cuántas "i", etc.
# Devolver un diccionario con los resultados.
# Desarrollar un programa para leer una frase e invocar a la función por cada palabra que contenga la misma.
# Imprimir cada palabra y la cantidad de vocales hallada.
# Frase: If you run into a wall and pretend it does not exist, you will never make any progress. The wall will never change, so you are the one who has to change


def contravocales(cadena):
    canta=cadena.count("a")
    cante=cadena.count("e")
    canti=cadena.count("i")
    dicc={"a":canta,
          "e":cante,
          "i":canti
          }
    return dicc


#Hay que agregar strip para comas y puntos tal vez
def main():
    frase=input("Ingrese una frase: ")
    cadfrase=frase.split()
    for palabra in cadfrase:
        print(palabra)
        diccvocal=contravocales(palabra.lower())
        print(f"A={diccvocal['a']}    E={diccvocal['e']}    I={diccvocal['i']}")
        print()


main()