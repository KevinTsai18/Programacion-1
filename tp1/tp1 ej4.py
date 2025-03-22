"""4.Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes
(detalladas en la tabla de abajo) se solicita desarrollar una función
que reciba como parámetro la cantidad de viajes realizados en un determinado mes
y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función."""

def calculartarifa(cantviaj):
    valor=int(input("Ingrese el valor del pasaje actualizado: "))
    tarifa=0
    if cantviaj<=20:
        tarifa=cantviaj*valor
        print(tarifa)
    elif cantviaj>20 and cantviaj<=30:
        tarifa=20*valor+(cantviaj-20)*valor*80/100
        print(tarifa)
    elif cantviaj>30 and cantviaj<=40:
        tarifa=20*valor+(cantviaj-20)*valor*80/100+(cantviaj-30)*valor*70/100
        print(tarifa)
    else:
        tarifa=20*valor+(cantviaj-20)*valor*80/100+(cantviaj-30)*valor*70/100+(cantviaj-40)*valor*60/100
        print(tarifa)

#PRINT HACERLO EN EL MAIN PORQUE NO TIENE QUE VER CON EL OBJETIVO LA FUNCION


def main():
    viajes=int(input("Ingrese la cantidad de viajes realizados: "))
    while viajes<=0:
        viajes=int(input("Cantidad inválida. Ingrese otra cantidad: "))
    totalgastado=calculartarifa(viajes)
    
main()