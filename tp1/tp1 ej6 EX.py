"""6.Escribir dos funciones para imprimir por pantalla cada uno de los siguientes patrones de asteriscos,
donde la cantidad de filas se recibe como parámetro:"""

#FUNCIONES

def ingresarPositivo():
    cantfilas=int(input("Ingrese la cantidad de filas que desea: "))
    while cantfilas<=0:
        cantfilas=int(input("Cantidad inválida. Ingrese otra: "))
    return (cantfilas)



def patron1(filas):
    cont=0
    while cont<filas:
        print("**********")
        cont=cont+1
        

def patron2(filas):
    for i in range(filas):
        for j in range(i+1):
            print("**", end="")
        print()


#PROG PPAL
def main():
    """Programa principal
    """
    cantfilas=ingresarPositivo()
    patron1(cantfilas)
    print("------------")
    patron2(cantfilas)

main()