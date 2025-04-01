# 5.Se dispone de tres formatos diferentes de archivos de texto
# en los que se almacenan datos de empleados.
# Los formatos se indican más abajo.
# Desarrollar un programa para cada uno de los formatos suministrados,
# que permitan leer cada uno de los archivos y grabar los datos obtenidos en otro archivo de texto con formato CSV.
# Archivo 1: Todos los campos son de longitud fija.
# Archivo 2: Los campos están separados por el signo #.
# Archivo 3: Todos los campos de este archivo están precedidos
# por un número de dos dígitos que indica la longitud del campo a leer.
# NOTA: Los espacios que se encuentren al final de las cadenas en el archivo 1 deberán ser eliminados.

def leerArchivo3():
    try:
        arch=open("archivo 3.txt",encoding="utf-8")
        datos=open("datos3.csv","w")
    except IOError:
        print("No se pudo abrir uno de los archivos.")
    else:
        reg=arch.readline()
        while reg!="":
            reg=reg.rstrip("\n")
            while reg!="":
                long=reg[:2]
                nombre=reg[2:2+int(long)]
                reg=reg[2+int(long):]
                long=reg[:2]
                legajo=reg[2:2+int(long)]
                reg=reg[2+int(long):]
                long=reg[:2]
                direccion=reg[2:2+int(long)]
                reg=reg[2+int(long):]
                datos.write(f"Nombre:{nombre}"+"\n")
                datos.write(f"N° Legajo:{legajo}"+"\n")
                datos.write(f"Dirección:{direccion}"+"\n")
            reg=arch.readline()
        arch.close()
        datos.close()


def main():
    leerArchivo3()

main()