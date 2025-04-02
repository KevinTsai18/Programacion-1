# Ejercicio 2:
# Cree un programa que ingrese primero el apellido y a continuación el nombre,
# deberá crear una cadena que contenga Apellido una coma un espacio y el
# Nombre (si tiene doble apellido o doble nombre, debe quedar con un solo
# espacio entre cada palabra). Luego se solicita que lo muestre por pantalla
# centrado (Considerando una pantalla con 80 columnas de ancho) y alternando
# mayúsculas y minúsculas por palabra. Ejemplo: Martinez, Juan Pedro
# MaRtInEz, JuAn PeDrO



nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
cadena=apellido+", "+nombre
cadenafinal=""
for i in range(len(cadena)):
    if i%2==0 and cadena[i].isalpha():
        cadenafinal=cadenafinal+cadena[i].upper()
    elif i%2!=0 and cadena[i].isalpha():
        cadenafinal=cadenafinal+cadena[i].lower()
    else:
        cadenafinal=cadenafinal+cadena[i]
print(cadenafinal)
print(cadenafinal.center(80))