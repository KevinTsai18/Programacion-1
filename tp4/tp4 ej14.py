"""14.Escribir un programa para crear una lista por comprensión
con los naipes de la baraja española. La lista debe contener cadenas de caracteres.
Ejemplo: ["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla. """

def main():
    naipes=[f"{nro} Oros" for nro in range(1,13)]+[f"{nro} Bastos" for nro in range(1,13)]+[f"{nro} Espadas" for nro in range(1,13)]+[f"{nro} Copas" for nro in range(1,13)]
    print(naipes)

main()