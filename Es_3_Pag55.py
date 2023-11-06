#Testo: Fare un programma dove: 1) Inizializzi "prima" e "seconda" con 2 numeri interi diversi
#2) Stampo i valori usando solo 1 f-string 3) Scambiare i valori 4) Stampare i nuovi valori

def main():
    n1 = int(input("Inserisci un numero intero: "))
    n2 = n1
    while n2 == n1:
        n2 = int(input("Inserisci un altro numero intero diverso: "))
    print(f"I valori sono {n1} e {n2}")

    #scambio
    n1, n2 = n2, n1
    print(f"I valori nuovi sono {n1} e {n2}")


if __name__ == "__main__":
    main()