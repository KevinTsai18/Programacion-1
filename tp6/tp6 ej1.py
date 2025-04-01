# 1.Desarrollar un programa para eliminar todos los comentarios de un programa
# escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el signo #
# (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
# y que también se considera comentario a las cadenas de documentación (docstrings).

def main():
    try:
        arch=open("prueba de python.txt")
        sincom=open("texto sin comentarios.txt","w")
    except IOError:
        print("No se pudo abrir el archivo.")
    else:
        registro=arch.readline()
        while registro!="":
            if registro[0]!="#" and registro[0]!="'" and registro[0]!='"':
                sincom.write(registro+"\n")
            elif (registro[0]=="'" and registro[len(registro)-1]=="'") or (registro[0]=='"' and registro[len(registro)-1]=='"'):
                registro=arch.readline()
                continue
            else:
                if "#" in registro:
                    poscom=registro.index("#")
                    if poscom!=0:
                        if registro[0:poscom].count("#")%2==0:
                            sincom.write(registro+"\n")
            registro=arch.readline()
        arch.close()
        sincom.close()

main()