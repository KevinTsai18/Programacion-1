# 9.Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 20 (ambos incluidos)
# y los valores asociados sean el cuadrado de las claves.

def generarDiccionario():
    dicc={}
    for i in range(1,21):
        dicc[i]=[i**2]
    return dicc


def main():
    dicc=generarDiccionario()
    for clave in dicc:
        print("Clave:", clave, "Valor:", dicc[clave])
    
main()