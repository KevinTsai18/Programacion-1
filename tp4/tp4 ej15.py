"""15.Muchas aplicaciones financieras requieren que los números sean expresados también en letras.
Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres".
Escribir un programa que utilice una función para convertir un número entero entre 0 y 1 billón
(1.000.000.000.000) a letras. ¿En qué cambiaría la función si también aceptara números negativos?
¿Y números con decimales?"""


def nroaletra(numero):
    cadnum=""
    nrosindiv=["","Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Once", "Doce", "Trece", "Catorce", "Quince", "Dieciseis", "Diecisiete", "Dieciocho", "Diecinueve", "Veinte"]
    decenas=["","", "Veinti", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"]
    centenas=["Cien","Ciento","Doscientos", "Trescientos", "Cuatroscientos", "Quinientos", "Seiscientos", "Setescientos", "Ochocientos", "Novescientos"]
    if numero<=20:
        cadnum=nrosindiv[numero]
    elif numero==1000000000000:
        cadnum="Un billón"
    while numero//10!=:
        if numero//1000000000==1:
            cadnum=cadnum+"Mil "
            numero=numero//10
        elif numero//1000000000!=0:
            cadnum=cadnum+f"{nrosindic[numero//1000000000]} mil"
            numero=numero//10
        if numero//100000000==1:
            cadnum=cadnum+"Mil"
            numero=numero//10
        elif numero//100000000!=0:
            cadnum=cadnum+f"{nrosindic[numero//1000000000]} mil"
            numero=numero//10
        



def main():
    numero=int(input("Ingrese el número para expresar en letras: "))
    cadnum=nroaletra(numero)
    print(cadnum)