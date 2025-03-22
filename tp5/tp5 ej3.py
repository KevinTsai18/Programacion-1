"""3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""


#HACER CONTROL DE NROS NEGATIVOS ANTES DE 

def numames(nro):
    try:
        meses=["","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        cadenames=meses[nro]
        if nro<0:
            print("Error. No se ha ingresado un número de mes válido.")
    except IndexError:
        cadenames=""
        print("Error. No se ha ingresado un número de mes válido.")
    return cadenames

def main():
    numeromes=int(input("Ingrese un número de mes: "))
    print(numames(numeromes))


main()