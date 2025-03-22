"""12.Utilizar la técnica de listas por comprensión para construir
una lista con todos los números impares comprendidos entre 100 y 200."""


def main():
    lista=[num for num in range(100,200) if num%2!=0]
    print(lista)
    
    
main()