# 13.Una librería almacena su lista de precios en un diccionario.
# Diseñar un programa para crearlo, incrementar los precios de los cuadernos en un 15%,
# imprimir un listado con todos los elementos de la lista de precios
# e indicar cuál es el ítem más costoso que venden en el comercio

def crearDiccionario():
    dicc={}
    elemento=input("Ingrese el elemento, o presione enter para terminar: ")
    while elemento!="":
        precio=int(input("Ingrese el precio: "))
        if "cuaderno" in elemento:
            precio=precio+precio/100*15
        dicc[elemento]=precio
        elemento=input("Ingrese el elemento, o presione enter para terminar: ")
    return dicc





def main():
    dicc=crearDiccionario()
    for clave in dicc:
        print(f"{clave} = ${dicc[clave]}")
    if dicc=={}:
        print("No hay elementos cargados.")
    else:
        preciomayor=0
        for clave in dicc:
            if dicc[clave]>preciomayor:
                clavemayor=clave
                preciomayor=dicc[clave]
        print("El elemento más caro es:",clavemayor)


main()