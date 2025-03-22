"""15.Muchas aplicaciones financieras requieren que los números sean expresados también en letras.
Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres".
Escribir un programa que utilice una función para convertir un número entero entre 0 y 1 billón
(1.000.000.000.000) a letras. ¿En qué cambiaría la función si también aceptara números negativos?
¿Y números con decimales?"""

import random
#ESCRIBIR NOMBRE DE ATRAS PARA ADELANTE E IR CONVIRTIENDO A INT PARA VER SI SE VA CAMBIANDO LAS LETRAS

def unideccen(numero):
    nrosindiv=["","Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Once", "Doce", "Trece", "Catorce", "Quince", "Dieciseis", "Diecisiete", "Dieciocho", "Diecinueve", "Veinte", "Veintiuno", "Veintidos", "Veintitres", "Veinticuatro", "Veinticinco", "Veintiseis", "Veintisiete", "Veintiocho", "Veintinueve"]
    decenas=["","", "", "Treinta", "Cuarenta", "Cincuenta", "Sesenta", "Setenta", "Ochenta", "Noventa"]
    centenas=["","Ciento","Doscientos", "Trescientos", "Cuatroscientos", "Quinientos", "Seiscientos", "Setescientos", "Ochocientos", "Novescientos"]
    cadnum=""
    cadena=""
    while numero!=0:
        numactual=numero%10
        numero=numero//10
        cadena=str(numactual)+cadena
        if int(cadena)<30 and numactual!=0:
            cadnum=nrosindiv[int(cadena)]
        elif int(cadena)<100 and numactual!=0:
            cadnum=decenas[numactual]+" y "+nrosindiv[int(cadena)%10]
            if int(cadena)%10==0:
                cadnum=cadnum.rstrip(" y")
        elif int(cadena)<1000 and numactual!=0:
            if int(cadena)==100:
                cadnum="Cien"
            else:
                cadnum=centenas[numactual]+" "+cadnum
    return cadnum


def nroaletra(numero):
    cadfinal=""
    if numero==1000000000000:
        cadfinal="Un billón"
    else:
        cont=0
        while numero!=0:
            if numero%1000!=0 and cont==0:
                cadfinal=unideccen(numero)
                numero=numero//1000
                cont+=1
            elif numero%1000!=0 and cont==1:
                if numero%10==1:
                    cadfinal=unideccen(numero).rstrip("o")+" Mil "+cadfinal
                    numero=numero//1000
                    cont+=1
                else:
                    cadfinal=unideccen(numero)+" Mil "+cadfinal
                    numero=numero//1000
                    cont+=1
                    if cadfinal[0:3]=="Uno":
                        cadfinal=cadfinal.lstrip("Uno ")
            elif numero%1000!=0 and cont==2:
                if unideccen(numero)=="Uno":
                    cadfinal="Un millón "+cadfinal
                    numero=numero//1000
                    cont+=1
                else:
                    if numero%10==1:
                        cadfinal=unideccen(numero).rstrip("o")+" Millones "+cadfinal
                        numero=numero//1000
                        cont+=1
                    else:
                        cadfinal=unideccen(numero)+" Millones "+cadfinal
                        numero=numero//1000
                        cont+=1
            elif numero%1000!=0 and cont==3:
                if numero%10==1:
                    cadfinal=unideccen(numero).rstrip("o")+" Mil Millones "+cadfinal
                    if cadfinal.count("Millones")>1:
                        cadfinal=cadfinal.replace("Millones ","",1)
                    if cadfinal[0:3]=="Uno":
                        cadfinal=cadfinal.lstrip("Uno ")
                    numero=numero//1000
                    cont+=1
                else:
                    cadfinal=unideccen(numero)+" Mil Millones"+" "+cadfinal
                    numero=numero//1000
                    if cadfinal.count("Millones")>1:
                        cadfinal=cadfinal.replace("Millones ","",1)
                    if cadfinal[0:3]=="Uno":
                        cadfinal=cadfinal.lstrip("Uno ")
                    cont+=1
            else:
                numero=numero//1000
                cont+=1
    return cadfinal



def main():
    #numero=int(input("Ingrese el número para expresar en letras: "))
    for i in range(10):
        numero=random.randint(1,100000000000)
        print(numero)
        cadnum=nroaletra(numero)
        print(cadnum)

main()