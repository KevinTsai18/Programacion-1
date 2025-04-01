# 3.Escribir una función que devuelva la suma de los N primeros números naturales

def sumaNat_rec(limite,n=1):
    if n>limite:
        return 0
    else:
        return n+sumaNat_rec(limite,n+1)


def main():
    limite=int(input("Ingrese el limite: "))
    print(sumaNat_rec(limite))

main()