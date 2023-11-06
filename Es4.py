#Programma che chieda all'utente due numeri float, il programma mi deve stampare una stringa con i due numeri in ordine decrescente.

a = float(input("Inserisci un numero"))
b = float(input("Inserisci un altro numero"))
if a<b:
   a, b = b, a
print(f"Ecco i numeri in ordine decrescente: {a}{b}")

