import pygame
#MANCA PYGAME

class Piastrella():
    def __init__(self, image):
        self.image = image
        self.rect = pygame.Rect(0, 0, 175, 175)

def numeraCelleLibere(groups):
    

def disegna(matrice):
    groups = matrice.replace('\n', '').split(" ")
    groups = [int(group) for group in groups]
    print(groups)
    for valore in groups:
        if valore == 1:
            print("Ciao")
        else:
            print("Addio")
    
    diz = {}
    k = 1
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0:
                matrice[indice_riga][indice_colonna] = k
                k += 1

    for indice_riga, riga in enumerate(pavimento):
        for indice_colonna, casella in enumerate(riga):
            if casella == 0:


def main():
    file = open("pavimento.txt", "r")
    listaNum = file.read()
    disegna(listaNum)
    numeraCelleLibere(groups)

if __name__ == "__main__":
    main()


#Celle blu sono celle libere, quelle rosse no. Scrivere una funzione che numeri le celle libere (A partire da 0). Fare dizionario adiacenze