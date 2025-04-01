def leerArchivo():
    '''
    Lee un archivo de texto con datos de empleados.
    Los campos de los registros están precedidos por un número
    de dos dígitos que indica la longitud del campo a leer
    Ejemplo:
    LongLegajo(2)LegajoLongNombre(2)NombreLongCateg(2)categoriaLongSueldo(2)sueldo
    0612312310Juan Perez01A0810000.01
    0610101014Pedro Gonzalez01B071010.09
    '''
    try:
        arch=open("empleados2.txt","rt")
    except IOError:
        print("No se pudo crear el archivo.")
    else:
        #Lee un registro
        suma=0
        registro=arch.readline()
        while registro!="":
            registro=registro.strip("\n")
            #print(registro)
            camposReg=registro.split(";")
            legajo,nombre,categoria,sueldo=camposReg

            print(f"Legajo:{legajo}\nNombre:{nombre}\nCategoria:{categoria}\nSueldo:{sueldo}")
            registro=arch.readline()
            #Lee el siguiente registro
        arch.close

leerArchivo()