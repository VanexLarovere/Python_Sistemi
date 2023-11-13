#Permettere all'utente di inserire due numeri qualsiasi, creare un dizionario dove ci si salva la media
#matematica e la media geometrica dei due numeri. Stampa poi il dizionario

def main():
    n1 = int(input("Inserisci il primo numero: "))
    n2 = int(input("Inserisci il secondo numero: "))

    media_mat = (n1 + n2) / 2
    if n1 < 0 or n2 < 0:
        print("La media geometrica ha bisongo di numeri non negativi")
    else:
        media_geom = (n1 * n2)**0.5

    risultati = {"Media Matematica": media_mat, "Media Geometrica": media_geom}

    print("Dizionario:", risultati)

if __name__ == "__main__":
    main()
