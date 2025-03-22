"""13.Escribir un programa para generar una lista con los múltiplos de 7
que no sean múltiplos de 5, entre 2000 y 3500. Imprimir la lista obtenida."""


def main():
    lista=[]
    for i in range(2000,3501):
        if i%7==0 and i%5!=0:
            lista.append(i)
    print(lista)


main()