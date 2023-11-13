#Permettere all'utente di inserire il suo nome e stampare la lista in cui gli elementi sono i 
#caratteri del nome

def main():
    nome = input("Inserisci il nome: ")
    lista = []

    for k in range(1, len(nome)):
        lista.append(nome[k])

    print(f"Lista: {lista}")

if __name__ == "__main__":
    main()
