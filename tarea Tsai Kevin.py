#Utilizar la técnica de listas por comprensión
#para construir una lista con el doble del valor
#de los numeros impares de un rango de números entre M y N inclusive.
#El valor de M y N se ingresa por teclado asegurando que exista un rango entre ellos.
#mostrar la lista creada por comprension pantalla



def main():
    num1=int(input("Ingrese un número: "))
    num2=int(input("Ingrese otro número: "))
    while num1==num2:
        num2=int(input("Rango inexistente. Ingrese otro número: "))
    if num1<num2:
        M=num1
        N=num2
    else:
        M=num2
        N=num1
    lista=[elem*2 for elem in range(M,N+1) if elem%2!=0]
    print(lista)

main()