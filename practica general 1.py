# Ejercicio 1: Desarrollar un programa que ingrese direcciones web
# y verifique si es una dirección válida, considerando que las
# direcciones web deberán:
# a.Comenzar con www.
# b.Continuar con caracteres alfanuméricos, guión medio, guión
# bajo en cualquier orden, al menos un caracter. (No puede
# comenzar con guiones, ni espacios)
# c.Finalizar con .com .edu .org puede contener a continuación . y
# dos caracteres alfabéticos representando un país.
# Finalizar el ingreso de direcciones web al no ingresar una cadena.
# Luego mostrar un listado en orden alfabético de todas las
# direcciones válidas ingresadas, sin repetir e informar cuántas
# pertenecen a Argentina. (Finalicen con “ar”)


def validarUrl(direccion):
    validez=True
    """
        Primero se ve si tiene la cantidad mínima de caracteres para poder analizar (www. + .com = 8 caracteres).
        Debe tener 9 caracteres mínimo.
    """
    if len(direccion)<9:
        validez=False
    elif direccion[0:4]!="www.":
        validez=False
    elif direccion[4]=="-" or direccion[4]==" " or direccion[4]=="_" or direccion[4]==".":
        validez=False
    elif "org" not in direccion.split(".") and "edu" not in direccion.split(".") and "com" not in direccion.split("."):
        validez=False
    return validez

def main():
    url=input("Ingrese la dirección web: ")
    listadir=[]
    while url!="":
        while validarUrl(url)==False:
            url=input("Dirección inválida. Ingrese otra dirección web: ")
        listadir.append(url)
        url=input("Ingrese la dirección web: ")
    listadir=set(listadir)
    listadir=list(listadir)
    listadir.sort()
    contar=0
    for direccion in listadir:
        print(direccion)
        if direccion[-2:]=="ar":
            contar+=1
    print(f"Hay {contar} direcciones de Argentina.")

main()
        
    