# 10.Escribir una función que reciba un número entero N
# y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12.
# Escribir también un programa para probar la función.

def generarDiccionario(n):
    dicc={}
    for i in range(1,13):
        dicc[i]=[n*i]
    return dicc



def main():
    n=int(input("Ingrese un número: "))
    dicc=generarDiccionario(n)
    print(f"Tabla de {n}:")
    for clave in dicc:
        print(f"{n} X {clave} = {dicc[clave]}")

main()