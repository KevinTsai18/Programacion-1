"""2.Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año.
Cada línea del archivo se grabará con el siguiente formato:
<dia>;<mes>;<lluvia caída en mm>  por ejemplo  25;5;319
Los datos se generarán mediante números al azar, asegurándose que las fechas sean válidas.
La cantidad de registros también será un número al azar entre 50 y 200.
Por último se solicita leer el archivo generado e imprimir un informe en formato matricial
donde cada columna represente a un mes y cada fila corresponda a los días del mes.
Imprimir además el total de lluvia caída en todo el año."""

from random import randint

def crearMatrizdiames():
    matriz=[]
    for f in range(31):
        matriz.append([])
        for c in range(12):
            matriz[f].append(0)
    return matriz


def imprimirMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            print("%3d" %matriz[fila][columna], end=" ")
        print()

def generarArchivo():
    try:
        arch=open("reporte lluvia.txt","w")
    except IOError:
        print("No se pudo abrir el archivo.")
    else:
        decidirlimite=input("Desea ingresar limite de lluvia? (y/n)")
        if decidirlimite.lower()=="y":
            limite=int(input("Ingrese el limite: "))
        else:
            limite=1000
        cantreg=randint(5,15)
        for i in range(cantreg):
            mes=randint(1,12)
            dia=randint(1,31)
            while (mes==4 or mes==6 or mes==9 or mes==11) and dia==31:
                dia=randint(1,30)
            while mes==2 and dia>29:
                dia=randint(1,28)
            lluvia=randint(0,limite)
            arch.write(str(dia)+";"+str(mes)+";"+str(lluvia)+"\n")
        arch.close()

def leerArchivo():
    arch=open("reporte lluvia.txt")
    matriz=crearMatrizdiames()
    reg=arch.readline()
    total=0
    while reg!="":
        camposReg=reg.split(";")
        matriz[int(camposReg[0])-1][int(camposReg[1])-1]=int(camposReg[2])
        total+=int(camposReg[2])
        reg=arch.readline()
    imprimirMatriz(matriz)
    print("El total de mm de lluvia que cayó en el año es:", total)
    arch.close()


def main():
    generarArchivo()
    leerArchivo()

main()
    