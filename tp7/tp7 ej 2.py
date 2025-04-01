# 2.Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.

#Se le puede dar por omision el valor inicial del parametro que servirá como contador
def binarioDecimal(binario,pos=0):
    if binario==0:
        return 0
    else:
        digito=binario%10
        termino=digito*2**pos
        return termino+binarioDecimal(binario//10,pos+1)


def main():
    numBin=1011
    decimal=binarioDecimal(numBin)
    print(f"el binario {numBin} en decimal es {decimal}")

main()


# 1011 --> digito*2**pos
# 1*2**0 + 1*2**1 + 0*2**2 + 1*2**3