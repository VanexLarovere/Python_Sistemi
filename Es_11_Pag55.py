#Testo: Inizializza la lista "x = [0, 1, 2, 3, 4, 5, 6, 7, 8]", crea 2 liste contenenti ciascuna una metà
#di questa lista, aggiungi 5 alla lista contenente la prima metà.

def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    l1 = []
    l2 = []
    l1 = x[0:5]
    l2 = x[5:-1]
    l1.append(5)
    print(f"La lista 1 è: {l1} \nMentre la lista 2 è: {l2}")


if __name__ == "__main__":
    main()