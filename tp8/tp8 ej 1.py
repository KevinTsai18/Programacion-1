# 1.Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios,
# y luego escribir un programa para verificar su comportamiento:
# a.Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.
# b.Sumar N días a una fecha.
# c.Ingresar un horario desde teclado, verificando que sea correcto.
# d.Calcular la diferencia entre dos horarios.
# Si el primer horario fuera mayor al segundo se considerará que el primero corresponde al día anterior.
# En ningún caso la diferencia en horas puede superar las 24 horas.


#calcular solo horas
#para primero mayor al segundo, 
def esBisiesto(añoF):
    respuesta=False
    if añoF%100==0 and añoF%400==0:
        respuesta=True
    elif añoF%4==0:
        respuesta=True
    return respuesta


def verificarfecha(diaF,mesF,añoF):
    """CHEQUEA SI LA FECHA ES VALIDA
    """
    fechavalida=True
    #numeros negativos
    if diaF<1 or mesF<1 or añoF<1:
        fechavalida=False
    #Chequeo mes
    elif mesF>12:
        fechavalida=False
    #Chequeo días
    elif mesF==1 or mesF==3 or mesF==5 or mesF==7 or mesF==8 or mesF==10 or mesF==12:
        if diaF>31:
            fechavalida=False
    elif mesF==4 or mesF==6 or mesF==9 or mesF==11:
        if diaF>30:
            fechavalida=False
    elif mesF==2:
        if (esBisiesto(añoF)):
            if diaF>29:
                fechavalida=False
        else:
            if diaF>28:
                fechavalida=False
    else:
        fechavalida=False
    return fechavalida


def sumardias(fecha,n,listameses):
    nuevodia=fecha[0]
    nuevomes=listameses.index(fecha[1])
    nuevoaño=fecha[2]
    while n!=0:
        nuevodia+=1
        n-=1
        if verificarfecha(nuevodia,nuevomes,nuevoaño)==False:
            if nuevomes==12:
                nuevoaño+=1
                nuevomes=1
                nuevodia=1
            else:
                nuevomes+=1
                nuevodia=1
    nuevafecha=(nuevodia,listameses[nuevomes],nuevoaño)
    return nuevafecha

def main():
    meses=("","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    año=int(input("Ingrese el año: "))
    while año<0:
        año=int(input("Ingrese otro año: "))
    mes=int(input("Ingrese el mes: "))
    while mes<1 or mes>12:
        mes=int(input("Ingrese otro mes: "))
    dia=int(input("Ingrese el día: "))
    while verificarfecha(dia,mes,año)==False:
        dia=int(input("Ingrese otro día: "))
    fecha=(dia,meses[mes],año)
    print(fecha)
    ndias=int(input("Ingrese una cantidad de días a sumas: "))
    fecha=sumardias(fecha,ndias,meses)
    print(fecha)
    horario1=int(input("Ingrese un horario: "))
    while horario1<0 or horario1>23:
        horario1=int(input("Ingrese un horario: "))
    horario2=int(input("Ingrese un horario: "))
    while horario2<0 or horario2>23:
        horario2=int(input("Ingrese un horario: "))
    if horario2>horario1:
        diferencia=horario2-horario1
    else:
        diferencia=24-horario1+horario2
    print(diferencia)
main()