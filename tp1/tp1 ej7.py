"""7.Desarrollar una función que reciba como parámetros dos números enteros
y devuelva el número que resulte de concatenar ambos valores.
Por ejemplo, si recibe 1234 y 567 debe devolver 1234567.
No se permite utilizar facilidades de Python no vistas en clase."""

def concatenar(num1,num2):
    aux=num2
    pot10=1
    while aux//10!=0:
        aux=aux//10
        pot10=pot10+1
    numconcat=num1*(10**pot10)+num2
    print(numconcat)
        


def main():
    x=int(input("Ingrese un número entero: "))
    y=int(input("Ingrese otro número entero: "))
    concatenar(x,y)
    
main()