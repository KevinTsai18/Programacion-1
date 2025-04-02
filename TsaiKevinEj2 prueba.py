# Ejercicio 2)
# Leer las frases del archivo frases.txt y crear un nuevo archivo con las palabras de cada registro sin repetirlas,
# ordenadas según su longitud. No considerar caracteres no alfabéticos para la longitud de la palabra.
# Al finalizar mostrar por pantalla un listado de las palabras en orden alfabético y cuantas veces aparece en todo el archivo.
# Recorda no cargar todo el archivo en memoria para resolver.

def sacarSimbolos(cadena):
    'Agrega a una nueva cadena solo los caracteres alfabéticos y los espacios para conservar las palabras.'
    nueva_cadena=""
    for letra in cadena:
        if letra.isalpha()==True or letra==" ":
            nueva_cadena=nueva_cadena+letra
    return nueva_cadena


def main():
    try:
        archivo_frases=open("frases.txt",encoding="utf-8")
        archivo_palabras=open("palabras prueba.txt","w")
    except IOError:
        print("No se pudo abrir uno de los archivos.")
    else:
        diccionario_palabras={}
        lista_palabras=[]
        registro=archivo_frases.readline()
        print(registro)
        while registro!="":
            registro=sacarSimbolos(registro)
            palabras=registro.split(" ")
            'Al convertirlo en conjunto se eliminan los elementos repetidos.'
            palabras=set(palabras)
            palabras=list(palabras)
            'Se asume que se ordenan de menor a mayor longitud.'
            palabras=sorted(palabras,key=lambda palabra:len(palabra))
            for palabra in palabras:
                archivo_palabras.write(palabra+" ")
                'Una vez que se escriba la palabra en el archivo nuevo, se pasa a minúscula para facilitar el conteo.'
                palabra=palabra.lower()
                if palabra not in lista_palabras:
                    lista_palabras.append(palabra)
                if palabra not in diccionario_palabras:
                    diccionario_palabras[palabra]=1
                else:
                    diccionario_palabras[palabra]+=1
            archivo_palabras.write("\n")
            registro=archivo_frases.readline()
        archivo_frases.close()
        archivo_palabras.close()
        lista_palabras.sort()
        for palabra in lista_palabras:
            print(f"Palabra : {palabra}  Apariciones : {diccionario_palabras[palabra]}")


main()