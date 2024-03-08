import random

class Nemico():  #Tutte pubbliche
    def __init__(self, posizione_x, posizione_y, n_vite):
        self.posizione_x = posizione_x
        self.posizione_y = posizione_y
        self.n_vite = n_vite
    
    def stampa(self):
        print(f"Nemico in posizione {self.posizione_x}, {self.posizione_y} con {self.n_vite} vite")

class Personaggio():
    def __init__(self):
        pass

def main():
    N_NEMICI = 5
    WIDTH = 500
    HEIGHT = 500
    lista_nemici = []
    random.seed(1234) #Seleziona il seme deterministico dei numeri pseudocasuali
    for _ in range(N_NEMICI): #Usiamo _ quando la variabile non ci serve
        pos_x = random.randint(0, WIDTH-1)
        pos_y = random.randint(0, HEIGHT-1)
        nemico = Nemico(pos_x, pos_y, 3)
        lista_nemici.append(nemico)
    print(lista_nemici)
    personaggio = {"Posizione_x":100, "Posizione_y":200}
    for nemico in lista_nemici:
        nemico.stampa()
        if(nemico.posizione_x == personaggio["Posizione_x"] and nemico.posizione_y == personaggio["Posizione_y"]):
            print("COLLISIONE")



if __name__ == "__main__":
    main()