# 14.Escribir una función buscarclave() que reciba como parámetros un diccionario y un valor,
# y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario.
# Comprobar el comportamiento de la función mediante un programa apropiado.

def crearDiccionario():
    dicc={}
    clave=input("Ingrese una clave: ")
    while clave!="":
        valor=input("Ingrese un valor: ")
        dicc[clave]=valor
        clave=input("Ingrese una clave: ")
    return dicc
        
        
        
def buscarclave(dicc,valor):
    listaclaves=[]
    for clave in dicc:
        if dicc[clave]==valor:
            listaclaves.append(clave)
    return listaclaves



def main():
    dicc=crearDiccionario()
    n=input("Ingrese el valor a buscar: ")
    listaclaves=buscarclave(dicc,n)
    print(listaclaves)

main()