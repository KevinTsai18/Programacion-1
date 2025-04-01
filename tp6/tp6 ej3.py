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

def GrabarRangoAlturas(arc_altura):
    deporte=input("Ingrese el nombre del deporte, o presione enter para terminar el ingreso: ")
    while deporte!="":
        arc_altura.write(deporte+"\n")
        altura=int(input("Ingrese la altura del atleta, o ingrese -1 para terminar: "))
        while altura!=-1:
            arc_altura.write(str(altura)+"\n")
            altura=int(input("Ingrese la altura del atleta, o ingrese -1 para terminar: "))
        deporte=input("Ingrese el nombre del deporte, o presione enter para terminar el ingreso: ")


def GrabarPromedio(arc_altura,arc_promedio):
    arc_altura=open("alturas.txt","r")
    registro=arc_altura.readline()
    cont=0
    promedio=0
    while registro:
        if str(registro).isdigit():
            promedio=registro+promedio
            cont+=1
        elif cont==0:
            arc_promedio.write(registro+"\n")
        else:
            arc_promedio.write(registro+"\n")
            promedio=promedio//cont
            arc_promedio.write(str(promedio)+"\n")
            cont=0
        registro=arc_altura.readline()

#def MostrarMasAltos():

def main():
    try:
        arc_altura=open("alturas.txt","w")
        arc_promedio=open("promedio alturas.txt","w")
        arc_altura=GrabarRangoAlturas(arc_altura)
        arc_promedio=GrabarPromedio(arc_altura,arc_promedio)
    except IOError:
        print("No se pudo crear el archivo.")
    else:
        arc_altura.close()
        arc_promedio.close()

main()
        
        