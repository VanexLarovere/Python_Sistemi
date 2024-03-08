import random
import turtle

LUNG = 10

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    percorso = {0: Punto(0,0)}
    bob = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(500, 500)

    for tempo in range(1, 60):
        #simulatore movimenti casuali
        scelta = random.randint(1, 4) #Scelta randomica tra 1 e 4
        #disegnare percorso con turtle
        if scelta == 1:
            percorso[tempo] = Punto(percorso[tempo-1].x, percorso[tempo-1].y - LUNG) #Nord, x di prima ed y cambiata
        if scelta == 2:
            percorso[tempo] = Punto(percorso[tempo-1].x, percorso[tempo-1].y + LUNG) #Sud
        if scelta == 3:
            percorso[tempo] = Punto(percorso[tempo-1].x - LUNG, percorso[tempo-1].y) #perché si parte da est
        if scelta == 4:
            percorso[tempo] = Punto(percorso[tempo-1].x + LUNG, percorso[tempo-1].y) #Ovest

        bob.goto(percorso[tempo].x, percorso[tempo].y)
        #BONUS controllo passaggio punto già visitato
    #scrittura su file del percorso
    #COLONNE: minuto, x, y
    with open("percorso.csv", "w") as file:
        for chiave in percorso:
            file.write(f"Minuto, PosX, PosY\n")

        for minuto in percorso:
            posx = percorso[minuto].x
            posy = percorso[minuto].y
            file.write(f"{minuto} {posx} {posy}\n")
    screen.mainloop()



if __name__ == "__main__":
    main()