"""4.Escribir una función que reciba como parámetro un número entero entre 0 y 3999
y lo convierta en un número romano, devolviéndolo en una cadena de caracteres.
¿En qué cambiaría la función si el rango de valores fuese diferente?"""



def pasarRomano(numero):
    romano=""
    largo=len(numero)
    cont=0
    pos=-1
    while cont<largo:
        if pos==-1:
            if int(numero[pos])<=3:
                romano="I"*int(numero[pos])+romano
            elif int(numero[pos])==4:
                romano="IV"+romano
            elif int(numero[pos])==9:
                romano="IX"+romano
            else:
                romano="V"+"I"*(int(numero[pos])-5)+romano
            cont+=1
            pos-=1
        elif pos==-2:
            if int(numero[pos])<=3:
                romano="X"*int(numero[pos])+romano
            elif int(numero[pos])==4:
                romano="XL"+romano
            elif int(numero[pos])==9:
                romano="XC"+romano
            else:
                romano="L"+"X"*(int(numero[pos])-5)+romano
            cont+=1
            pos-=1
        elif pos==-3:
            if int(numero[pos])<=3:
                romano="C"*int(numero[pos])+romano
            elif int(numero[pos])==4:
                romano="CD"+romano
            elif int(numero[pos])==9:
                romano="CM"+romano
            else:
                romano="D"+"C"*(int(numero[pos])-5)+romano
            cont+=1
            pos-=1
        else:
            romano="M"*int(numero[pos])+romano
            cont+=1
            pos-=1
    return romano



def main():
    numero=input("Ingrese el número a pasar a romano: ")
    if not numero.isdigit():
        numero=input("Ingrese el número a pasar a romano: ")
    romano=pasarRomano(numero)
    print(romano)


main()