import turtle


def main():
    lista = []
    fermo = 1
    n = 0
    while fermo != 0:
        com = input("Inserisci il comando tra F (Dritto), R (Destra), L (Sinistra), 0 per uscire: ")
        lista.append(com)
        n = n+1

    finestra = turtle.screen()
    tarta = turtle.Turtle()
    

if __name__ == "__main__":
    main()