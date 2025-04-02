# 5. En geometría un vector es un segmento de recta orientado que va desde un punto A hasta un punto B.
# Los vectores en el plano se representan mediante un par ordenado de números reales (x, y) llamados componentes.
# Para representarlos basta con unir el origen de coordenadas con el punto indicado en sus componentes: 
# Dos vectores son ortogonales cuando son perpendiculares entre sí.
# Para determinarlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo: 
# A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
# Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor de verdad
# indicando si son ortogonales o no. Desarrollar también un programa que permita verificar el comportamiento de la función.


def esOrtogonal(v1,v2):
    perpend=False
    if v1[0]*v2[0]+v1[1]*v2[1]==0:
        perpend=True
    return perpend


def main():
    vector1_1=int(input("Ingrese la coord x del primer vector: "))
    vector1_2=int(input("Ingrese la coord y del primer vector: "))
    vector2_1=int(input("Ingrese la coord x del segundo vector: "))
    vector2_2=int(input("Ingrese la coord y del segundo vector: "))
    vector1=(vector1_1,vector1_2)
    vector2=(vector2_1,vector2_2)
    if esOrtogonal(vector1,vector2):
        print("Son ortogonales.")
    else:
        print("No son ortogonales")


main()