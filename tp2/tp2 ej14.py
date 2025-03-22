"""14.Repetir el ejercicio anterior, pero utilizando la técnica de listas por comprensión.
"""

def main():
    lista=[num for num in range(2000,3500) if num%7==0 and num%5!=0]
    print(lista)
    

main()