"""3.Los números de claves de dos cajas fuertes están intercalados dentro de un número entero
llamado "clave maestra", cuya longitud no se conoce.
Realizar un programa para obtener ambas claves, donde la primera se construye
con los dígitos impares de la clave maestra y la segunda con los dígitos pares.
Los dígitos se numeran desde la izquierda. Ejemplo: Si clave maestra = 18293,
la clave 1 sería 123 y la clave 2 sería 89."""



def main():
    clavem=input("Ingrese la clave maestra: ")
    clave1=""
    clave2=""
    for n in range(len(clavem)):
        if n%2==0:
            clave1=clave1+clavem[n]
        else:
            clave2=clave2+clavem[n]
    print(clave1)
    print(clave2)

main()