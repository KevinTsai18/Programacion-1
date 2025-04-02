# Ingresar una cadena dentro de una función recursiva que la devuelva al revés

def invertirCad(cadena):
    """Ingresa una cadena y la devuelve invertida
    """
    if cadena=="":
        return ""
    else:
        return cadena[-1]+invertirCad(cadena[:-1])





def main():
    """Programa principal
    """
    cadena="hola que Andy Kamita"
    print(invertirCad(cadena))



main()