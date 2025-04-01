# 7.Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo Común Divisor
# (también llamado Divisor Común Mayor) basándose en las siguientes propiedades:
# MCD(X, X)= X
# MCD(X, Y)= MCD(Y, X)
# Si X > Y => MCD(X, Y) = MCD(X–Y, Y).

def mcd(x,y):
    if x<0 or y<0:
        return -1
    if x==y:
        return x
    else:
        if x>y:
            return mcd(x-y,y)
        else:
            #Se aplica propiedad conmutativa para cambiar de lugar y que a la izquierda quede como mayor
            return mcd(y,x)

def main():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print(mcd(n1,n2))

main()