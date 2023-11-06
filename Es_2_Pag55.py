#Testo: Inizializzare 4 variabili con l'assegnazione multipla(1 int, 1 stringa, 1 float, 1 bool) 
#e stampare il loro valore con il loro tipo usando type()


def main():
    n1, n2, n3, n4 = 8, "ciao", 0.7, True #Assegnazione multipla, la uso per assegnare a + variabili in una sola riga (Non so se va bene)

    print(f"Valore 1 : {n1}, tipo: {type(n1)}")
    print(f"Valore 2 : {n2}, tipo: {type(n2)}")
    print(f"Valore 3 : {n3}, tipo: {type(n3)}")
    print(f"Valore 4 : {n4}, tipo: {type(n4)}")



if __name__ == "__main__":
    main()