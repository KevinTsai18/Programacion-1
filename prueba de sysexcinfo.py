import sys

try:
    nro=int(input("Ingrese numero"))
except:
    print("Error.", sys.exc_info())