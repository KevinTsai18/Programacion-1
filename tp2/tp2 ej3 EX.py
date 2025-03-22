#TP2 - EJ3

#.Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
#donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

#Funciones
cuadrado=lambda x:x**2

#Programa principal
def main():
    lista=[]
    n=int(input("Ingrese un número: "))
    for i in range(1,n+1):
        lista.append(cuadrado(i))
    if len(lista)<10:
        for elem in lista:
            print(elem, end=" ")
    else:
        for j in range(-10,0):
            print(lista[j], end=" ")
        
    


main()