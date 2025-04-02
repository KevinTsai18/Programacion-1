# 4.Escribir una función que indique si dos fichas de dominó encajan o no.
# Las fichas son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4).
# La función devuelve True o False. Escribir también un programa para verificar su comportamiento

def encaje(p1,p2):
    encaja=False
    if (p1[0]==p2[0] or p1[0]==p2[1]) or (p1[1]==p2[0] or p1[1]==p2[1]):
        encaja=True
    return encaja



def main():
    pieza1_1=int(input("Ingrese uno de los números de la primer pieza: "))
    pieza1_2=int(input("Ingrese el otro número de la primer pieza: "))
    pieza2_1=int(input("Ingrese uno de los números de la segunda pieza: "))
    pieza2_2=int(input("Ingrese el otro número de la segunda pieza: "))
    pieza1=(pieza1_1,pieza1_2)
    pieza2=(pieza2_1,pieza2_2)
    if encaje(pieza1,pieza2):
        print("Las piezas encajan.")
    else:
        print("No encajan.")
    
main()