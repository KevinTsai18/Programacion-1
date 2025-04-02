# Escribir una funcion recursiva que busque el max y min de una lista


def buscarMaxMin(lista):
    """Ingresa lista de numeros y devuelve el valor mínimo y máximo como una tupla
    """
    if len(lista)==0:
        raise ValueError("La lista llegó vacía")
    elif len(lista)==1:
        return (lista[0],lista[0])
    else:
        (minimo,maximo)=buscarMaxMin(lista[1:])
        if lista[0]<minimo:
            minimo=lista[0]
        if lista[0]>maximo:
            maximo=lista[0]
    return (minimo,maximo)
    
    



def main():
    lista=[4,3,5,7,2]
    lista1=[4]
    lista0=[]
    try:
        print(buscarMaxMin(lista))
    except ValueError as mensaje:
        print(mensaje)



main()