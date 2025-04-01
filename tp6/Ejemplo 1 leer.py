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
        arch=open("empleados.txt","rt")
    except IOError:
        print("No se pudo crear el archivo.")
    else:
        #Lee un registro
        suma=0
        registro=arch.readline()
        while registro!="":
            registro=registro.strip("\n")
            #print(registro)
            long=int(registro[0:2])
            #Si o si hay que pasar a integral la longitud
            legajo=(registro[2:long])
            #Ahora se puede cortar el registro para que se tomen los primeros 2 para la longitud y el dato siguientes
            registro=registro[2+long:]
            
            #Ahora para el nombre
            long=int(registro[0:2])
            nombre=(registro[2:long])
            registro=registro[2+long:]
            
            #categoria
            long=int(registro[0:2])
            categoria=(registro[2:long])
            registro=registro[2+long:]
            
            
            
            #sueldo
            long=int(registro[0:2])
            sueldo=(registro[2:long])
            registro=registro[2+long:]
            
            print(f"Legajo:{legajo}\nNombre:{nombre}\nCategoria:{categoria}\nSueldo:{sueldo}")
            
            registro=arch.readline()
            #Lee el siguiente registro
        arch.close

leerArchivo()