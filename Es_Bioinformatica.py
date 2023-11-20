#Il file covid-19_gen1.txt contiene la sequenza del genoma del virus SARS-CoV-2. Esso è una sequenza di lettere (A, C, G, T) che corrispondono ai quattro nucleotidi costituenti: adenina (A), timina (T), guanina (G) e citosina (C) .
#Crea un programma in linguaggio Python 3 nel quale:
#leggi tutte le righe del file e le inserisci all’interno di un sola stringa che contenga l’intera sequenza genomica;
#stampi il numero di occorrenze dei quattro nucleotidi all’interno della sequenza;
#cerchi la sequenza iniziale ("ATGTTTGTTTTT") che codifica la proteina spike nel genoma: se presente allora stampa la posizione iniziale della sequenza.
def main():
    nomeFile = "covid-19_gen1.txt"
    listaSequenza = "ATGTTTGTTTTT"
    nA, nT, nG, nC = 0, 0, 0, 0

    file = open(nomeFile, "r")
    listaCar = file.read()

    for k in listaCar:
        if k == "A":
            nA += 1
        elif k == "T":
            nT += 1
        elif k == "G":
            nG += 1
        elif k == "C":
            nC += 1
        
        if k == "\n":
            k.replace("\n", "")
    #riga = riga[:-1] per sostituire la messa a capo
    print(f"Occorrenze\nA: {nA}\nT: {nT}\nG: {nG}\nC: {nC}")

    #Altro modo per contare i nucleotidi:

    #dizNucleotidi = {"A": 0, "C": 0, "G": 0, "T": 0}
    #for char in stringa:
    #    dizNucleotidi[char] += 1
    #return dizNucleotidi

    #Oppure

    #return len(x for x in stringa if x == nucleotide)


    j = 0
    while j + 12 <= len(listaCar): #12 = lunghezza listaSequenza
        listaControllo = listaCar[j:j+12] #Prende da j a j+12 (Lunghezza listaSequenza) 
        if listaControllo == listaSequenza:
            print(f"Trovato in posizione {j}")
        j += 1 #Devo controllare carattere per carattere perché se vado a gruppi di 12 potrebe esserci la combinazione con la lettera del gruppo prima

if __name__ == "__main__":
    main()