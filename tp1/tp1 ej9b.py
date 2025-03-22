"""9.Escribir una función diasiguiente(…) que reciba como parámetro
una fecha cualquiera expresada por tres enteros (correspondientes al día, mes y año)
y calcule y devuelva tres enteros correspondientes el día siguiente al dado.
Utilizando esta función, desarrollar programas que permitan:

b.Calcular la cantidad de días existentes entre dos fechas cualesquiera."""

def diasiguiente(d,m,a):
    cont=0
    daux=int(input("Ingrese otro dia: "))
    maux=int(input("Ingrese otro mes: "))
    aaux=int(input("Ingrese otro año: "))
    if a<aaux:
        d1=d
        d2=daux
        m1=m
        m2=maux
        a1=a
        a2=aaux
    elif a>aaux:
        d1=daux
        d2=d
        m1=maux
        m2=m
        a1=aaux
        a2=a
    elif a==aaux and m<maux:
        d1=d
        d2=daux
        m1=m
        m2=maux
        a1=a
        a2=aaux
    elif a==aaux and m>maux:
        d1=daux
        d2=d
        m1=maux
        m2=m
        a1=aaux
        a2=a
    elif a==aaux and m==maux and d<daux:
        d1=d
        d2=daux
        m1=m
        m2=maux
        a1=a
        a2=aaux
    elif a==aaux and m==maux and d>daux:
        d1=daux
        d2=d
        m1=maux
        m2=m
        a1=aaux
        a2=a
    else:
        print("Las fechas son iguales.")
    while d1!=d2 or m1!=m2 or a1!=a2:
        if m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10:
            if d1+1>31:
                m1=m1+1
                d1=1
                cont=cont+1
            else:
                d1=d1+1
                cont=cont+1
        elif m1==4 or m1==6 or m1==9 or m1==11:
            if d1+1>30:
                m1=m1+1
                d1=1
                cont=cont+1
            else:
                d1=d1+1
                cont=cont+1
        elif m1==12:
            if d1+1>31:
                m1=1
                d1=1
                a1=a1+1
                cont=cont+1
            else:
                d1=d1+1
                cont=cont+1
        elif m1==2:
            if (a1%4==0 and a1%100!=0) or a1%400==0:
                if d1+1>29:
                    m1=m1+1
                    d1=1
                    cont=cont+1
                else:
                    d1=d1+1
                    cont=cont+1
            else:
                if d1+1>28:
                    m1=m1+1
                    d1=1
                    cont=cont+1
                else:
                    d1=d1+1
                    cont=cont+1
    return cont

def main():
    dia=int(input("Ingrese el día de la fecha: "))
    mes=int(input("Ingrese el mes de la fecha: "))
    año=int(input("Ingrese el año de la fecha: "))
    diasinter=diasiguiente(dia,mes,año)
    print("La cantidad de días entre esas fechas es", diasinter)

main()