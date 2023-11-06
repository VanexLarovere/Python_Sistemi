def main():
    operaz = int(input("Inserisci l'operazione che vuoi eseguire: 0. Somma 1. Sottrazione 2. Moltiplicazione 3. Divisione"))
    n1 = int(input("Inserisci il primo numero: "))
    n2 = int(input("Inserisci il secondo numero: "))
    if operaz == 0:
        operaz = "somma"
        ris = n1 + n2
    else:
        if operaz == 1:
            operaz = "sottrazione"
            ris = n1 - n2
        else:
            if operaz == 2:
                operaz = "moltiplicazione"
                ris = n1 * n2
            else:
                if operaz == 3:
                    operaz = "Divisione"
                    ris = n1 / n2
                else:
                    print("Numero non valido, inserire tra 0-1-2-3")
    print(f"L'operazione compiuta è {operaz} ed il risultato è {ris}")            

if __name__ == "__main__":
    main()
