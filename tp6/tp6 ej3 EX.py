"""3.Una institución deportiva necesita clasificar a sus atletas para inscribirlos
en los próximos Juegos Panamericanos. Para eso encargó la realización de un programa que incluya las siguientes funciones:
GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de distintas disciplinas,
los que se ingresan desde el teclado. Cada dato se debe grabar en una línea distinta.
Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >

<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
< . . . >

GrabarPromedio() Graba en un archivo los promedios de las alturas de los atletas
presentes en el archivo generado en el paso anterior.
La disciplina y el promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>

<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >

MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo."""

def GrabarRangoAlturas():
    try:
        arc_altura=open("alturas.txt","w")
    except IOError:
        print("No se pudo crear el archivo.")
    else:
        deporte=input("Ingrese el nombre del deporte, o presione enter para terminar el ingreso: ")
        while deporte!="":
            arc_altura.write(deporte+"\n")
            altura=int(input("Ingrese la altura del atleta, o ingrese -1 para terminar: "))
            while altura!=-1:
                arc_altura.write(str(altura)+"\n")
                altura=int(input("Ingrese la altura del atleta, o ingrese -1 para terminar: "))
            deporte=input("Ingrese el nombre del deporte, o presione enter para terminar el ingreso: ")
    arc_altura.close()


def GrabarPromedio():
    try:
        arc_altura=open("alturas.txt")
        arc_promedio=open("promedio alturas.txt","w")
    except IOError:
        print("No se pudo crear el archivo.")
    else:
        registro=arc_altura.readline()
        cont=0
        promedio=0
        while registro!="":
            registro=registro[0:len(registro)-1]
            if str(registro).isdigit():
                promedio=int(registro)+promedio
                cont+=1
            elif (str(registro).isalpha() or str(registro).isalnum()) and cont==0:
                arc_promedio.write(registro+"\n")
            elif cont!=0:
                promedio=promedio//cont
                arc_promedio.write(str(promedio)+"\n")
                cont=0
                promedio=0
                arc_promedio.write(registro+"\n")
            registro=arc_altura.readline()
        promedio=promedio//cont
        arc_promedio.write(str(promedio)+"\n")
        cont=0
    arc_altura.close()
    arc_promedio.close()

def MostrarMasAltos():
    try:
        arc_promedio=open("promedio alturas.txt")
        arc_alturas=open("alturas.txt")
    except IOError:
        print("No se pudo abrir el archivo.")
    else:
        registro=arc_promedio.readline()
        cont=0
        promedio=0
        while registro!="":
            registro=registro[0:len(registro)-1]
            if str(registro).isdigit():
                promedio=int(registro)+promedio
                cont+=1
            registro=arc_promedio.readline()
        promedio=promedio//cont
        registro=arc_alturas.readline()
        contprint=0
        while registro!="":
            registro=registro[0:len(registro)-1]
            if str(registro).isdigit()==False:
                deporte=registro
                contprint=0
            else:
                if int(registro)>promedio and contprint==0:
                    print(f"Hay atletas del deporte {deporte} que superan el promedio")
                    contprint=1
            registro=arc_alturas.readline()
        arc_alturas.close()
        arc_promedio.close()        
        

def main():
#        GrabarRangoAlturas()
        GrabarPromedio()
        MostrarMasAltos()



main()
        
        
