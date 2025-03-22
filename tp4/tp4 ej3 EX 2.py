"""3.Los números de claves de dos cajas fuertes están intercalados dentro de un número entero
llamado "clave maestra", cuya longitud no se conoce.
Realizar un programa para obtener ambas claves, donde la primera se construye
con los dígitos impares de la clave maestra y la segunda con los dígitos pares.
Los dígitos se numeran desde la izquierda. Ejemplo: Si clave maestra = 18293,
la clave 1 sería 123 y la clave 2 sería 89."""

def obtener_claves(string):
    '''Toma una contraseña maestra en string y obtiene
    los elementos de las posiciones impares o pares, admite letras'''
    clave1=[string[i] for i in range(0,len(string),2)]
    clave2=[string[i] for i in range(1,len(string),2)]
    return(clave1,clave2)


def main():
    clave=input("Ingrese cadena: ")
    clave1,clave2=obtener_claves(clave)
    print(clave1)
    print(clave2)

main()