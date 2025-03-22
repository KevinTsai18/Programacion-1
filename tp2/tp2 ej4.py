"""4.Definir una función superposición() que reciba como parámetros dos listas de cualquier tipo
y devuelva True si tienen al menos un elemento en común,
o False en caso contrario. Desarrollar un programa para verificar su comportamiento.
"""

import random

def superposicion(v1,v2):
    comun=False
    for i in range(len(v1)-1):
        for j in range(len(v2)-1):
            if v1[i]==v2[j]:
                comun=True
    return comun



def main():
    lista1=[]
    lista2=[]
    for i in range(10):
        lista1.append(random.randint(1,99))
        lista2.append(random.randint(1,99))
    print(lista1)
    print(lista2)
    if superposicion(lista1,lista2):
        print("Tienen elementos en común.")
    else:
        print("NO tienen elementos en común.")

main()
        