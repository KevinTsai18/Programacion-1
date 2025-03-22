"""2.Desarrollar una función que reciba tres números enteros positivos
y verifique si corresponden a una fecha gregoriana válida (día, mes, año).
Devolver True o False según la fecha sea correcta o no.
Realizar también un programa para verificar el comportamiento de la función."""


#FUNCIONES
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



def main():
    """PROGRAMA PRINCIPAL
    """
    DIA=int(input("Ingrese el número de día."))
    MES=int(input("Ingrese el número del mes."))
    AÑO=int(input("Ingrese el número de año."))
    fecha=verificarfecha(DIA,MES,AÑO)
    if fecha==True:
        print("La fecha es válida")
    else:
        print("La fecha NO es válida")

#PROG PPAL
main()
    