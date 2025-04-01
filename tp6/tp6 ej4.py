# 4. Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato
# "Apellido, Nombre" y guarde en el archivo ARMENIA.TXT los nombres de aquellas personas
# cuyo apellido terminan con la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI"
# y en el archivo ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:

# Arslanian, Gustavo –> ARMENIA.TXT Rossini, Giuseppe –> ITALIA.TXT Pérez, Juan –> ESPAÑA.TXT Smith, John –> descartar
# El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No escribir un programa para generarlo.



def leerArchivo():
    try:
        arch=open("inmigrantes.txt")
        archArm=open("ARMENIA.txt","w")
        archIta=open("ITALIA.txt","w")
        archEsp=open("ESPAÑA.txt","w")
    except IOError:
        print("No se pudo abrir el archivo.")
    else:
        reg=arch.readline()
        while reg!="":
            reg=reg.strip("\n")
            reg=reg.split(", ")
            if reg[0][-3:]=="ian":
                archArm.write(", ".join(reg)+"\n")
            elif reg[0][-3:]=="ini":
                archIta.write(", ".join(reg)+"\n")
            elif reg[0][-2:]=="ez":
                archEsp.write(", ".join(reg)+"\n")
            reg=arch.readline()
        arch.close()
        archArm.close()
        archIta.close()
        archEsp.close()


def main():
    leerArchivo()

main()