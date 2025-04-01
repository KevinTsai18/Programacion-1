# Ejercicio a Resolver:
# 
# 1.     Desarrollar un programa para crear una matriz de NxN con números al azar de tres dígitos positivos
#         (100 y 999) sin repetidos. 
#         N se solicita del teclado y se debe validar que sea positivo y menor a 20.
#         Mostrar por pantalla la matriz creada con formato de matriz.
#         La funcion para crear y/o rellenar la matriz debe ser genérica
#         y poder crear matrices de cualquier dimensión y rango de elementos. 
#         Utilizar los parámetros por omisión para el rango indicado del programa.
# 
# Informar:
# 
# a.  Crear una lista con los números impares de la matriz triangular superior
#     (considerando los números que se encuentran en la diagonal principal)
#      Adjunto tiene una imagen donde se indica cuál es la triangular superior con la diagonal principal incluída. 
#      Desarrollar y utilizar una función lambda para determinar si un número es impar.
#      Utilizar técnica de rebanadas para cada fila para obtener los valores solicitados.
# 
# b.  Crear otra lista por comprensión con los elementos de la diagonal principal e
#     informar el menor número. Cuántas veces aparece el menor número en la triángular superior?
# 
# c.   Concatenar ambas listas, ordenarlas y luego quitar de la lista los elementos
#     con digito central en cero utilizando la función filter para resolverlo.


from random import randint

# Funciones

esImpar=lambda x:True if x%2!=0 else False
'Permite determinar si un número que se recibe como parámetro es par o no.'

def crearMatriz(fila,columna,desde=100,hasta=999):
    """
        La función crea una fila de NxN
         - N = fila_columna
         El rango de los elementos por omisión es desde 100 a 999
         
    """
    # DEBERÍA PODER CREAR CUALQUIER TIPO DE MATRIZ!!!
    listaElementos=[]
    matriz=[]
    for f in range(fila):
        matriz.append([])
        for c in range(columna):
            elemento=randint(desde,hasta)
            while elemento in listaElementos:
                elemento=randint(desde,hasta)
            listaElementos.append(elemento)
            matriz[f].append(elemento)
    #print(matriz)
    return matriz

def mostrarMatrizFormato(matriz):
    'Muestra por pantalla la matriz que recibe como parámetro.'
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print("%5d" %matriz[fila][columna], end=" ")
        print()

def obtenerTriangularSup(matriz):
    """
        Permite obtener la matriz triangular superior (incluyendo a la diagonal principal)
        de una matriz que se recibe como parámetro.
        
    """
    triangular_sup=[]
    limite=0
    while limite<len(matriz):
        triangular_sup=triangular_sup+matriz[limite][limite:len(matriz)]
        limite+=1
    return triangular_sup


def obtenerImpares(lista):
    'Crea una lista con los elementos impares de una lista.'
    lista_impares=[]
    for numero in lista:
        if esImpar(numero):
            lista_impares.append(numero)
    #print(lista_impares)
    return lista_impares


# Programa principal    

def main():
    fila=int(input("Ingrese la cantidad de filas y columnas para la matriz entre 1 y 20: "))
    while fila<1 or fila>20:
        fila=int(input("Cantidad inválida. Ingrese otra positiva menor a 20: "))
    columna=fila
    matriz=crearMatriz(fila,columna)
    mostrarMatrizFormato(matriz)
    #Se considera la diagonal principal como parte de la matriz triangular superior.
    matriz_triangular_sup=obtenerTriangularSup(matriz)
    lista_impares=obtenerImpares(matriz_triangular_sup)
    print("Los elementos impares de la matriz triangular superior son: ", lista_impares)
    lista_diagonal=[matriz[i][i] for i in range(len(matriz))]
    elemento_menor=min(lista_diagonal)
    print("El menor numero de la diagonal principal es: ", elemento_menor)
    print("Dicho elemento se encuentra", matriz_triangular_sup.count(elemento_menor), "veces dentro de la matriz triangular superior")
    lista_concatenada=lista_impares+lista_diagonal
    #print(lista_concatenada)
    lista_concatenada.sort() #Se considera el orden de menor a mayor.
    #print(lista_concatenada)
    lista_filtrada=list(filter(lambda numero:numero%100>=10,lista_concatenada))
    print("La lista concatenada, ordenada y sin los elementos que tienen cero como dígito central es: ", lista_filtrada)
    

main()