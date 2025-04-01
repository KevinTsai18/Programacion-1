# 4.Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas

def sumaSuc_rec(numero,limite):
    if limite==0:
        return 0
    else:
        return numero+sumaSuc_rec(numero,limite-1)


def main():
    prod1=int(input("Ingrese un numero entero: "))
    prod2=int(input("Ingrese otro numero entero: "))
    print(sumaSuc_rec(prod1,prod2))



main()