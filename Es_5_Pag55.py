#Testo: Assegnata una parola ad una variabile stringa, stampare tutto tranne il 1° e ultimo carattere

def main():
    stringa = input("Inserisci una parola: ")
    print(stringa[1:-1]) #Stampa tutti i caratteri tranne il 1° e l'ultimo

if __name__ == "__main__":
    main()