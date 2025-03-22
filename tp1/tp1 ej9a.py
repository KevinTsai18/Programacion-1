"""9.Escribir una función diasiguiente(…) que reciba como parámetro
una fecha cualquiera expresada por tres enteros (correspondientes al día, mes y año)
y calcule y devuelva tres enteros correspondientes el día siguiente al dado.
Utilizando esta función, desarrollar programas que permitan:

a.Sumar N días a una fecha."""

def diasiguiente(d,m,a,n):
    aux=n
    while n!=0:
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10:
            if n+d>31:
                m=m+1
                n=n-(31-d)
                d=0
            else:
                d=d+n
                n=0
        elif m==4 or m==6 or m==9 or m==11:
            if n+d>30:
                m=m+1
                n=n-(30-d)
                d=0
            else:
                d=d+n
                n=0
        elif m==12:
            if n+d>31:
                m=1
                n=n-(31-d)
                d=0
                a=a+1
            else:
                d=d+n
                n=0
        elif m==2:
            if (a%4==0 and a%100!=0) or a%400==0:
                if n+d>29:
                    m=3
                    n=n-(29-d)
                    d=0
                else:
                    d=d+n
                    n=0
            else:
                if n+d>28:
                    m=3
                    n=n-(28-d)
                    d=0
                else:
                    d=d+n
                    n=0
    print("La fecha que da al sumar", aux, "es", d,"/",m, "/", a)
        

def main():
    dia=int(input("Ingrese el día de la fecha: "))
    mes=int(input("Ingrese el mes de la fecha: "))
    año=int(input("Ingrese el año de la fecha: "))
    n=int(input("Ingrese la cantidad de días que desea sumar: "))
    diasiguiente(dia,mes,año,n)


main()