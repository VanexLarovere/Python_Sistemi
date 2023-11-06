#Testo: Assegnare una parola ad una variabile stringa e stampare solo i caratteri con indice dispari

def main():
    s = input("Inserisci una parola: ")
    lista = []
    n = -1
    for n in s[0]:
        if s[n] % 2 != 0:
            lista.append(s[n]) #Metto tutti i carattere nell'indice dispari in una lista
    
    #oppure
    print(s[1::2]) #Stampa i caratteri dispari
    print(f"{lista}") #Stampo la lista


if __name__ == "__main__":
    main()
