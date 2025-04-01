def ingresarLegajo():
    '''Ingresar un legajo por teclado, validar que sea positivo.
    Retorna entero'''
    while True:
        try:
            leg=int(input("Ingrese un legajo:"))
            while leg<=0:
                leg=int(input("Error. Número menor a 1. Ingrese otro:"))
            break
        except ValueError:
            print("Error ingreso de datos")
    return leg

def ingresarCategoria():
    '''Ingresar una categoria desde el teclado, validar que sea A,B,C
    Retorna cadena'''
    while True:
        try:
            categ=input("Ingrese la categoría (A,B,C):")
            while categ.upper() not in ("A","B","C"): #Recordar que es posible que ingresen minuscula tambien
                categ=input("Ingrese la categoría (A,B,C):")
            break
        except ValueError:
            print("Error de ingreso.")
    return categ

def ingresarSueldo():
    while True:
        try:
            sueldo=int(input("Ingrese un sueldo:"))
            while sueldo<=0:
                sueldo=int(input("Error. Número menor a 1. Ingrese otro:"))
            break
        except ValueError:
            print("Error ingreso de datos")
    return sueldo

def grabarConLongitudVariable():
    '''
    Graba un archivo de texto con datos de empleados.
    Los campos de los registros están precedidos por un número
    de dos dígitos que indica la longitud del campo a leer
    Ejemplo:
    LongLegajo(2)LegajoLongNombre(2)NombreLongCateg(2)categoriaLongSueldo(2)sueldo
    0612312310Juan Perez01A0810000.01
    0610101014Pedro Gonzalez01B071010.09
    '''
# Los datos pueden hasta venir en distinto orden cuando se ingresa
    try:
        arch=open("empleados.txt","w")
    except IOError as mensaje:
        print("Error de Entrada/Salida:", mensaje)
    else:
        nombre=input("Ingrese nombre:")
        while nombre!="":
            legajo=ingresarLegajo()
            categoria=ingresarCategoria()
            sueldo=ingresarSueldo()
            categoria=categoria.upper()
            nombre=nombre[:99]
            camposReg=[str(legajo),nombre,categoria,str(sueldo)]
            registro=""
            for campo in camposReg:
                registro+=f'{len(campo)}{campo}'
            arch.write(registro+'\n')
            nombre=input("Ingrese el nombre:")
            
def main():
    grabarConLongitudVariable()

main()