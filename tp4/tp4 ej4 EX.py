#Funciones
def romano(num):
    '''Toma un numero en sistema decimal y lo convierte en romano, el máximo es 3999'''
    if (num<0 or num>3999):
        nuevacad="Num no válido"
    elif(num==0):
        nuevacad="NULLA"
    else:
        mil=['','M','MM','MMM']
        centena=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        decena=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        unidad=['','I','II','III','IV','V','VI','VII','VIII','IX']
        m=num//1000
        c=(num-1000*m)//100
        d=(num-1000*m-100*c)//10
        u=(num-1000*m-100*c-d*10)//1
        nuevacad=mil[m]+centena[c]+decena[d]+unidad[u]
    return nuevacad

 

#Funcion princiapl
def main():
    '''Programa princiapl
    '''
    num=int(input("Ingrese un número decimal para convertirlo en romano: "))
    print("El romano es: ",end=" ")
    numrom=romano(num)
    print(numrom)

main()