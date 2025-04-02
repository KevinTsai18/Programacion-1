# Ejercicio 8: Se ingresan los legajos (4 dígitos) y las notas (1-
# 10) de los alumnos de un curso hasta ingresar un legajo -1.
# Ingresar alternando legajo-nota. No solicitar una nota si se
# ingresa legajo -1.
# Crear un archivo alumnos.csv en el orden en que fueron
# ingresados con el legajo y su nota correspondiente e indicando
# su estado (Aprobado o Desaprobado), los campos del archivo
# son de longitud fija; 6 lugares para el legajo, y 2 lugares para la
# nota, 12 lugares para el estado.
# 1010__10Aprobado__ los_ representan espacios


def main():
    try:
        arch=open("alumnos.csv","w")
    except IOError:
        print("No se pudo abrir el archivo.")
    else:
        legajo=input("Ingrese el n° de legajo")
        while legajo!="-1":
            nota=input("Ingrese la nota: ")
            if int(nota)<4:
                estado="Desaprobado"
            else:
                estado="Aprobado   "
            if nota=="10":
                arch.write(legajo+"  "+nota+estado+"\n")
            else:
                arch.write(legajo+"  0"+nota+estado+"\n")
            legajo=input("Ingrese el n° de legajo")
    arch.close()

main()