lista1 = []
lista2 = []
prog = True
while prog == True:
    print("Scrivi le parole che vuoi aggiunte alla lista oppure premi 0 se vuoi uscire: ")
    parola1 = input()
    if parola1 == "0":
        prog = False
    else:
        lista1.append(parola1)
cont = len(lista1)
for i in range(cont):
    num2 = len(lista1[i])
    lista2.append(num2)
print(lista2)