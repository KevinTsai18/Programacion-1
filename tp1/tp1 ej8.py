"""8.Escribir una función que reciba como parámetro número del 1 al 9 y
devuelva el resultado de sumar n + nn + nnn + nnnn,
donde n corresponde al número recibido.
Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333).
Escribir también un programa para verificar el comportamiento de la función.
No se permite utilizar facilidades de Python no vistas en clase."""



def sumamultiple(num):
    n=num
    nn=num*10+num
    nnn=num*100+num*10+num
    nnnn=num*1000+num*100+num*10+num
    resultado=n+nn+nnn+nnnn
    print(resultado)






def main():
    n=int(input("Ingrese un número del 1 al 9: "))
    sumamultiple(n)
    
main()