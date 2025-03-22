"""11.Escribir un programa que permita ingresar una cadena de caracteres
y coloque en mayúscula la primera letra posterior a un espacio,
eliminando todos los espacios que contenga. Imprimir por pantalla la cadena obtenida.
Ejemplo: Cadena original: Platero es pequeño, peludo, suave;
tan blando por fuera, que se diría todo de algodón, que no lleva huesos.
Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Cadena final:
PlateroEsPequeño,Peludo,Suave;TanBlandoPorFuera,
QueSeDiríaTodoDeAlgodón,QueNoLlevaHuesos.
SóloLosEspejosDeAzabacheDeSusOjosSonDurosCualDosEscarabajosDeCristalNegro."""


def main():
    frase=input("Ingrese una cadena de caracteres: ")
    frase=frase.title()
    cad=""
    for i in range(len(frase)):
        if frase[i]!=" ":
            cad=cad+frase[i]
    print(cad)



main()