"""4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt.
Realizar un programa para imprimir los números enteros entre 1 y 100000,
y que solicite confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""

def impresionnros():
    for i in range(100000):
        try:
            print(i+1)
        except KeyboardInterrupt:
            resp=input("Quiere continuar? 's=si/n=no'")
            while resp!="s" and resp!="n":
                resp=input("Respuesta inválida. Ingrese s para si o n para no.")
            if resp.lower()=="n":
                break


def main():
    impresionnros()


main()