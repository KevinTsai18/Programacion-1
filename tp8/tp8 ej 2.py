# 2.Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año)
# y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido.
# Por ejemplo, para (12,10,17) devuelve "12 de Octubre de 2017".
# Escribir también un programa para verificar su comportamiento.

def tuplaFechaCadena(fecha):
     meses=["","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
     cadena=f"{fecha[0]} de {meses[fecha[1]]} de {fecha[2]}"
     return cadena


def main():
    año=int(input("Ingrese el año: "))
    while año<0:
        año=int(input("Ingrese otro año: "))
    mes=int(input("Ingrese el mes: "))
    while mes<1 and mes>12:
        mes=int(input("Ingrese otro mes: "))
    dia=int(input("Ingrese un día: "))
    while dia<1:
        dia=int(input("Ingrese otro día: "))
    while (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia>31:
        dia=int(input("Ingrese otro día: "))
    while (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        dia=int(input("Ingrese otro día: "))
    if mes==2:
        if (año%100==0 and año%400==0) or año%4==0:
            while dia>29:
                dia=int(input("Ingrese otro día: "))
        else:
            while dia>28:
                dia=int(input("Ingrese otro día: "))
    fecha=(dia,mes,año)
    fechacad=tuplaFechaCadena(fecha)
    print(fechacad)

main()