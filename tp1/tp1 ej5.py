"""5.Un comercio de electrodomésticos necesita para su línea de cajas
un programa que le indique al cajero el cambio que debe entregarle al cliente.
Para eso se ingresan dos números enteros, correspondientes al total de la compra
y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto,
de tal forma que se minimice la cantidad de billetes.
Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente.
Ejemplo: Si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100,
1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.
"""


def calcularcambio(dincomp,dinrec):
    vuelto=dinrec-dincomp
    print("La cantidad de billetes que se le debe dar de vuelto son: ")
    while vuelto!=0:
        if vuelto//500!=0:
            print(vuelto//500, "billetes de 500")
            vuelto=vuelto%500
        elif vuelto//100!=0:
            print(vuelto//100, "billetes de 100")
            vuelto=vuelto%100
        elif vuelto//50!=0:
            print(vuelto//50, "billetes de 50")
            vuelto=vuelto%50
        elif vuelto//20!=0:
            print(vuelto//20, "billetes de 20")
            vuelto=vuelto%20
        elif vuelto//10!=0:
            print(vuelto//10, "billetes de 10")
            vuelto=vuelto%10
        elif vuelto//5!=0:
            print(vuelto//5, "billetes de 5")
            vuelto=vuelto%5
        elif vuelto//1!=0:
            print(vuelto//1, "billetes de 1")
            vuelto=0


def main():
    compra=int(input("Ingrese el total de la compra: "))
    dinero=int(input("Ingrese la cantidad de dinero recibida: "))
    if dinero<compra:
        print("El dinero recibido no es suficiente.")
    elif dinero==compra:
        print("No hay que darle cambio")
    else:
        calcularcambio(compra,dinero)

main()