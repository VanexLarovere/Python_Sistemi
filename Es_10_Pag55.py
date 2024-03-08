#Testo: Assegnare alla lista "lista_voti" tutti i miei voti (Almeno 6). 1) Stampare la lista senza il primo e ultimo voto
#2) Sostituire il quarto voto con un 10 3) Stampare i primi 3 voti della lista

def main():
    lista = []
    k=0

    while True:
            voto = int(input("Inserisci un voto(-1 per interrompere): "))
            if(voto < 0 and k>= 6):
                break
                lista.append(voto)
                k = 1

    print(f"Lista senza il 1° e l'ultimo voto: {lista[1:-1]}")
    lista[3] = 10
    print(f"Lista con il 4° voto sostituito con un 10: {lista}")
    print(f"Lista con solo i primi 3 voti: {lista[0:3]}") #Stampo dal primo carattere al 3 incluso

if __name__ == "__main__":
    main()
