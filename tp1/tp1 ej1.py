#1.Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres,
#sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1.
#No utilizar operadores lógicos (and, or, not).
#Desarrollar también un programa para ingresar los tres valores,
#invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe."""

def ordenar(v):
    largo=len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i]<v[j]:
                aux=v[i]
                v[i]=v[j]
                v[j]=aux
    return v

def buscarmayor(a,b,c):
    lista=[]
    lista.append(a)
    lista.append(b)
    lista.append(c)
    print(lista)
    lista=ordenar(lista)
    if lista[0]==lista[1]:
        mayorestricto=-1
    else:
        mayorestricto=lista[0]
    return mayorestricto

def main():
    x=int(input("Ingrese un número:"))
    while x<=0:
        x=int(input("El número ingresado no es válido. Por favor ingrese otro."))
    y=int(input("Ingrese otro número:"))
    while y<=0:
        y=int(input("El número ingresado no es válido. Por favor ingrese otro."))
    z=int(input("Ingrese un número más:"))
    while z<=0:
        z=int(input("El número ingresado no es válido. Por favor ingrese otro."))
    resultado=buscarmayor(x,y,z)
    if resultado==-1:
        print("No hay un número mayor estricto")
    else:
        print(resultado)

main()

