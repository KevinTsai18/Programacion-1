"""5.Escribir una función filtrar_palabras()
que reciba una cadena de caracteres conteniendo una frase y un entero N,
y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función,
para cada uno de los siguientes casos:
c.Utilizando la función filter"""

def filtrar_palabras(cadena,N):
    lista=cadena.split(" ")
    nuevacad=list(filter(lambda palabra:len(palabra)>=N,lista))
    return nuevacad
    
    
    



def main():
    frase=input("Ingrese una frase: ")
    cantidad=int(input("Ingrese un número entero positivo: "))
    nuevacad=filtrar_palabras(frase,cantidad)
    print(nuevacad)

main()