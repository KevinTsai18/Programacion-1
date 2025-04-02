# Ingresar una cadena y mediante una funcion recursiva ver si tiene mas vocales que consonantes.


def masVocCons(cadena,i=0):  #i=relacion de cantidad de vocales MENOS cantidad de consonantes
    """Ingresa una cadena y devuelve si tiene mas vocales que consonantes
    """
    'Interesa ver si hay mas cantidad de vocales que de consonantes (LA RELACION), no la cantidad en sí'
    if len(cadena)==0:
        'Si i es positivo, hay mas vocales'
        return(i>0)
    """Se puede meter una condicion dentro del return que devuelve True o False dependiendo de si se cumple la condicion
    """
    
#         if i>0:
#             resp=True
#         else:
#             resp=False
#         return resp
    else:
        vocales=["a","e","i","o","u","A","E","I","O","U"]
        cant=i
        if cadena[0] in vocales:
            cant+=1
        elif cadena[0].isalpha():
            cant-=1
        return masVocCons(cadena[1:],cant)



def main():
    cadena="edificio"
    print(masVocCons(cadena))




main()