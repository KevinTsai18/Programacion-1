"""5.Escribir una función filtrar_palabras()
que reciba una cadena de caracteres conteniendo una frase y un entero N,
y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función,
para cada uno de los siguientes casos:
a.Utilizando sólo ciclos normales"""

def filtrar_palabras(cadena,N):
    lista=cadena.split(" ")
    nuevacad=""   #Inicializo cadena vacía
    for palabra in lista:
        if len(palabra)>=N:
            nuevacad=nuevacad+palabra+" "
    return nuevacad
    



def main():
    frase=input("Ingrese una frase: ")
    cantidad=int(input("Ingrese un número entero positivo: "))
    nuevacad=filtrar_palabras(frase,cantidad)
    print(nuevacad)

main()