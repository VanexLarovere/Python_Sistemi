lettere = "abcdefghilmnopqrstuvz"
lettere2numeri = {}
numeri2lettere = {}
#print(len(lettere))
for posizione, lettera in enumerate(lettere):
    print(posizione, lettera)
    lettere2numeri[lettera] = posizione
    numeri2lettere[posizione] = lettera

print(" ")
testo_chiaro = "persia"
chiave = "itisdelpozzo"

for lettera in testo_chiaro:
    #print(lettera) #Mi stampa ciascuna lettera
    print(lettere2numeri[lettera]) #index della lettera

for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave):
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave])
    print(numero)
#RIPASSARE SPLIT E JOIN, SCRIVERE SU FILE E LEGGERE DA FILE, una funzione mai usata, classi, dizionari, cicli sui dizionari, creare dizionari..., funzioni

testo_chiaro = "persia"
chiave = "itisdelpozzo"

for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave):
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave])
    print(numero)