# Ejercicio 1)
# Direcciones web: Se solicita un programa para ingresar direcciones web hasta ingresar una cadena vacía.
# Resolver utilizando while-true y creando o generando una excepción para rechazar las cadenas que no corresponden a una dirección web.
# Una dirección web válida consideramos que comienza con http:// o https:// pero no siempre, ya que también puede comenzar con www,
# sigue el nombre del sitio que no puede ser vacío y luego tiene uno o dos puntos.
# Tener en cuenta que no siempre tiene terminación referenciando al código del país.
# Ejemplo: www.organizacion.com.ar, https://www.organizacion2.edu, http://www.ejemplo.edu
# Al finalizar el ingreso informar:
# Listado de dominios que aparecen más de una vez ordenado alfabéticamente,
# indicando cuantas veces se ingresaron. Recorda que el dominio se refiere al tipo de organizacion y país, segun el ejemplo seria:
# Dominio     Cantidad
# edu                2
# com.ar             1
# Informar también la cantidad de direcciones web no válidas.

#Se crean las excepciones.
class ComienzoInvalido(Exception):
    pass

class NombreInvalido(Exception):
    pass

class TerminacionInvalida(Exception):
    pass

def evaluarNombreSitio(direccion):
    'Evalua si el nombre del sitio está vacío o no, fijándose si hay un punto más después del comienzo (sin contar el de www.).'
    nombre_valido=True
    if direccion[:11]=="http://www." and direccion[11]==".":
        nombre_valido=False
    elif direccion[:12]=="https://www." and direccion[12]==".":
        nombre_valido=False
    elif direccion[:4]=="www." and direccion[4]==".":
        nombre_valido=False
    return nombre_valido


def evaluarTerminacion(direccion):
    """Evalua si la terminación ocupa la cantidad de caracteres correspondiente.
        - Para la organización, deben ser 3 caracteres.
        - Para el país, 2 caracteres.
        En caso de tener más de 3 puntos o menos de 2 puntos se tomará como inválido también.
    """
    
    terminacion_valida=True
    lista=direccion.split(".")
    if len(lista)==3:
        if len(lista[2])!=3:
            terminacion_valida=False
    elif len(lista)==4:
        if len(lista[2])!=3 or len(lista[3])!=2:
            terminacion_valida=False
    else:
        terminacion_valida=False
    return terminacion_valida
                


def main():
    contador_invalidos=0
    lista_direccion=[]
    while True:
        try:
            direccion=input("Ingrese una direccion web o presione enter para dejar de ingresar: ")
            if direccion=="":
                break
            #Se asume que después de http// o https// siempre habrá un www.
            if direccion[:11]!="http://www." and direccion[:12]!="https://www." and direccion[:4]!="www.":
                raise ComienzoInvalido("El comienzo de la direccion ingresada es inválido.")
            if evaluarNombreSitio(direccion)==False:
                raise NombreInvalido("El nombre de la direccion es inválido.")
            if evaluarTerminacion(direccion)==False:
                raise TerminacionInvalida("La terminación de la dirección es inválida.")
        except (ComienzoInvalido,NombreInvalido,TerminacionInvalida) as mensaje:
            print("Error",mensaje)
            contador_invalidos=contador_invalidos+1
        else:
            lista_direccion.append(direccion)
    #print(lista_direccion)
    diccionario_direccion={}
    for direccion in lista_direccion:
        lista_partes=direccion.split(".")
        'Si tiene dominio con pais y organizacion, se juntan para facilitar el conteo.'
        if len(lista_partes)==4:
            lista_partes[2]=lista_partes[2]+"."+lista_partes[3]
            del lista_partes[3]
        #print(lista_partes)
        'Se evalua si está repetido el dominio o no.'
        if lista_partes[2] not in diccionario_direccion:
            diccionario_direccion[lista_partes[2]]=1
        else:
            diccionario_direccion[lista_partes[2]]+=1
    print("Dominio".ljust(15," ")+"Cantidad")
    for dominio in diccionario_direccion:
        if diccionario_direccion[dominio]!=1:
            print(dominio.ljust(15," "),str(diccionario_direccion[dominio]).center(8," "))
    print(f"La cantidad de direcciones web inválidas que se ingresaron fueron: {contador_invalidos}")



main()