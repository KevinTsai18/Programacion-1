# 6.Ídem anterior, pero determinando si los vectores son paralelos.
# Cuando dos vectores son paralelos los cocientes de sus coordenadas correspondientes son iguales entre sí.
# Ejemplo: U = (3,-1) y V = (-9,3)


def esParalelo(v1,v2):
    paralelo=False
    if v1[0]/v2[0]==v1[1]/v2[1]:
        paralelo=True
    return paralelo


def main():
    vector1_1=int(input("Ingrese la coord x del primer vector: "))
    vector1_2=int(input("Ingrese la coord y del primer vector: "))
    vector2_1=int(input("Ingrese la coord x del segundo vector: "))
    vector2_2=int(input("Ingrese la coord y del segundo vector: "))
    vector1=(vector1_1,vector1_2)
    vector2=(vector2_1,vector2_2)
    if esParalelo(vector1,vector2):
        print("Son paralelos.")
    else:
        print("No son paralelos")


main()