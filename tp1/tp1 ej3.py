"""3.Para un número entero N menor de 100 recibido como parámetro,
escribir un programa que utilice una función para devolver
la suma de los cuadrados de aquellos números entre 1 y N que están separados entre si por cuatro unidades.
(1**2 + 5**2 + 9**2 + 13**2 + …)"""

def sumacuadrados(num):
    suma=0
    cont=1
    while cont<=num:
        suma=cont**2+suma
        cont=cont+4
    return suma



def main():
    n=int(input("Ingrese un número entero menor a 100."))
    while n<0 or n>100:
        n=int(input("Número inválido. Ingrese otro número."))
    resultado=sumacuadrados(n)
    print(resultado)



main()