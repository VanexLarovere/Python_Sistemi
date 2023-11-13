#Permettere all'utente di inserire il suo nome e stampare il nome in cui tutti i caratteri tranne il primo
#sono sostituiti con un *

def main():
    nome = input("Inserisci il nome: ")

    nome = nome[0] + '*' * (len(nome)-1)

    print(f"Nome finale: {nome}")

if __name__ == "__main__":
    main()