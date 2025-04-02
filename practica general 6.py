# Ejercicio 6:
# Desarrolla una función llamada agregarUnicos(lista, valor) que reciba una
# lista y un elemento. La función debe añadir el elemento al final de la lista
# con la condición de no repetir ningún elemento. Además, si este elemento
# ya se encuentra en la lista se debe invocar un error de tipo ValueError que
# se debe capturar y mostrar este mensaje en su lugar:
# Error: Imposible agregar elementos duplicados => [elemento].
# Crear un programa principal para agregar crear una lista de palabras
# Que se ingresan por teclado. Rechazar las palabras repetidas. Considerar
# Repetidas las palabras aunque difieran en mayúscula/minuscula

def crearlista():
    lista=[]
    palabra=input("Ingrese una palabra.")
    while palabra!="":
        if len(lista)==0:
            lista.append(palabra)
        else:
            repetido=False
            for i in range(len(lista)):
                if palabra.lower()==lista[i].lower():
                    repetido=True
            if repetido==False:
                lista.append(palabra)
            else:
                print("Error. Palabra repetida.")
        palabra=input("Ingrese una palabra.")
    return lista


def agregarUnicos(lista,valor):
    try:
        for i in range(len(lista)):
            if valor.lower()==lista[i].lower():
                raise ValueError(f"Error: Imposible agregar elementos duplicados => {valor}")
    except ValueError as mensaje:
        print(mensaje)
        lista=[]
    else:
        lista.append(valor)
        return lista


def main():
    lista=crearlista()
    if len(lista)==0:
        print("La lista esta vacía.")
    else:
        print(lista)
        valor=input("Ingrese una palabra a agregar a la lista: ")
        lista=agregarUnicos(lista,valor)
        if len(lista)==0:
            print("No se pudo agregar.")
        else:
            print(lista)

main()