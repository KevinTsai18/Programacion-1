


lista=[str(j+1)+" "+i  for i in ["OROS","BASTOS","ESPADAS","COPAS"]  for j in range(12)]
print(lista)

#por palo

#Según el orden de los for cambia como se hace la lista

lista=[str(j+1)+" "+i for j in range(12) for i in ["OROS","BASTOS","ESPADAS","COPAS"]]
print(lista)

#Por numero