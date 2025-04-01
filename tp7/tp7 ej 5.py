# 5.Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.

def restaSuc_rec(n1,n2):
    if n1-n2<0:
        return n1
    else:
        return restaSuc_rec(n1-n2,n2)



def main():
    num1=int(input("Ingrese un número: "))
    num2=int(input("Ingrese otro número: "))
    print(restaSuc_rec(num1,num2))

main()