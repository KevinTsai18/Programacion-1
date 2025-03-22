"""2.Desarrollar una función que reciba tres números enteros positivos
y verifique si corresponden a una fecha gregoriana válida (día, mes, año).
Devolver True o False según la fecha sea correcta o no.
Realizar también un programa para verificar el comportamiento de la función."""

#FUNCIONES
def verificarfecha(diaF,mesF,añoF):
    """CHEQUEA SI LA FECHA ES VALIDA
    """
    fechavalida=True
    if mesF==1 or mesF==3 or mesF==5 or mesF==7 or mesF==8 or mesF==10 or mesF==12:
        if diaF>31:
            fechavalida=False
    elif mesF==4 or mesF==6 or mesF==9 or mesF==11:
        if diaF>30:
            fechavalida=False
    elif mesF==2:
        if (añoF%4==0 and añoF%100!=0) or añoF%400==0:
            if diaF>29:
                fechavalida=False
        else:
            if diaF>28:
                fechavalida=False
    else:
        fechavalida=False
    return fechavalida



def main():
    """PROGRAMA PRINCIPAL
    """
    DIA=int(input("Ingrese el número de día."))
    while DIA<0:
        DIA=int(input("Número inválido. Ingrese otro número entero positivo."))
    MES=int(input("Ingrese el número del mes."))
    while MES<0:
        MES=int(input("Número inválido. Ingrese otro número entero positivo."))
    AÑO=int(input("Ingrese el número de año."))
    while AÑO<0:
        AÑO=int(input("Número inválido. Ingrese otro número entero positivo."))
    fecha=verificarfecha(DIA,MES,AÑO)
    if fecha==True:
        print("La fecha es válida")
    else:
        print("La fecha NO es válida")

#PROG PPAL
main()
    