"""13.Escribir un programa que cuente cuántas veces se encuentra una subcadena
dentro de otra cadena, sin diferenciar mayúsculas y minúsculas.
Tener en cuenta que los caracteres de la subcadena no necesariamente
deben estar en forma consecutiva dentro de la cadena, pero sí respetando el orden de los mismos.
Ejemplo:
Cadena: Platero es pequeño, peludo, suave; tan blando por fuera,
que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de
sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón,
que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
"""

def buscarSub(cad,sub):
    cantsubcad=0
    cont=0
    for i in range(len(cad)):
        if sub[cont]==cad[i].upper() or sub[cont]==cad[i].lower():    # Se puede poner if sub[cont].upper()==cad[i].upper()  Compara directamente
            cont+=1
            if cont==len(sub)-1:
                cont=0
                cantsubcad+=1
    return cantsubcad
        



def main():
    cadena=input("Ingrese una cadena de caracteres: ")
    subcad=input("Ingrese la subcadena: ")
    cantsub=buscarSub(cadena,subcad)
    print(cantsub)


main()