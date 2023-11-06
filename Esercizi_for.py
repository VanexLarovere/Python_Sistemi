lista = [4, 100, 3, 5, "ciao", print] #lista

#Per ciclare la lista possiamo usare un Ciclo for C-style
for i in range(0, len(lista)): #len serve per vedere la lunghezza della lista
    print(f"L'elemento [i]-esimo della lista è {lista[i]}")

#Ciclo for Python-style (Quello giusto da fare)
for elemento in lista:
    print(f"Elemento: {elemento}")