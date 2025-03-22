"""10.La siguiente función permite averiguar el día de la semana para una fecha determinada.
La fecha se suministra en forma de tres parámetros enteros
y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc.
Escribir un programa para imprimir por pantalla el calendario de un mes completo,
correspondiente a un mes y año cualquiera basándose en la función suministrada.
Considerar que la semana comienza en domingo.

def diadelasemana(dia,mes,año):
    if mes < 3:
        mes = mes + 10
        año = año – 1
    else:
        mes = mes – 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem"""


def diadelasemana(dia,mes,año):
    if mes<3:
        mes=mes+10
        año=año-1
    else:
        mes=mes-2
    siglo=año//100
    año2=año%100
    diasem=(((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem<0:
        diasem=diasem+7
    return diasem



def main():
    m=int(input("Ingrese el mes: "))
    a=int(input("Ingrese el año: "))
    d=1
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        while d<=31:
            ds=diadelasemana(d,m,a)
            if ds==0:
                ds="dom."
            elif ds==1:
                ds="lun."
            elif ds==2:
                ds="mar."
            elif ds==3:
                ds="mie."
            elif ds==4:
                ds="jue."
            elif ds==5:
                ds="vie."
            elif ds==6:
                ds="sab."
            print(d, "/", ds)
            d=d+1
    elif m==4 or m==6 or m==9 or m==11:
        while d<=30:
            ds=diadelasemana(d,m,a)
            if ds==0:
                ds="dom."
            elif ds==1:
                ds="lun."
            elif ds==2:
                ds="mar."
            elif ds==3:
                ds="mie."
            elif ds==4:
                ds="jue."
            elif ds==5:
                ds="vie."
            elif ds==6:
                ds="sab."
            print(d, "/", ds)
            d=d+1
    elif m==2:
        if (a%4==0 and a%100!=0) or a%400==0:
            while d<=29:
                ds=diadelasemana(d,m,a)
                if ds==0:
                    ds="dom."
                elif ds==1:
                    ds="lun."
                elif ds==2:
                    ds="mar."
                elif ds==3:
                    ds="mie."
                elif ds==4:
                    ds="jue."
                elif ds==5:
                    ds="vie."
                elif ds==6:
                    ds="sab."
                print(d, "/", ds)
                d=d+1
        else:
            while d<=28:
                ds=diadelasemana(d,m,a)
                if ds==0:
                    ds="dom."
                elif ds==1:
                    ds="lun."
                elif ds==2:
                    ds="mar."
                elif ds==3:
                    ds="mie."
                elif ds==4:
                    ds="jue."
                elif ds==5:
                    ds="vie."
                elif ds==6:
                    ds="sab."
                print(d, "/", ds)
                d=d+1
main()
