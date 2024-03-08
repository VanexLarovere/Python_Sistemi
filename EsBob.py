#Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a
#casa. Purtroppo Bob soffre di momentanee perdite di memoria!
#Questa volta la sua amnesia dura ben 60 minuti e durante questi 60 minuti Bob adotta la
#seguente strategia per tentare di rientrare a casa. Ogni minuto decide a caso tra:
#1. procedere 10 m verso Nord
#2. procedere 10 m verso Sud
#3. procedere 10 m verso Est
#4. procedere 10 m verso Ovest
#Simula l’intero percorso compiuto da Bob, supponendo che il punto di partenza abbia
#coordinate (0,0) e salvalo all’interno di un dizionario opportunamente strutturato.
#Disegna il percorso compiuto da Bob dentro una schermata di pygame oppure turtle, decidi
#tu quale libreria usare.
#Infine salva il percorso di Bob dentro un file .csv opportunamente strutturato.
import random
import turtle

#Come trovare la posizione del turtle: position()

LATO = 10

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def percorso(bobLista, amnesia, bob, file):
    x, y = 0, 0
    listaPercorso = []
    for cont in bobLista:
        if cont == 1:
            bob.setheading(90) #Nord
        if cont == 2:
            bob.setheading(270) #Sud
        if cont == 3:
            bob.setheading(0) #perché si parte da est
        if cont == 4:
            bob.setheading(180) #Ovest

        bob.pendown() #Poso la penna
        bob.forward(LATO)
        print(f"Coordinate: {bob.position()}")
        file.write(f"Coordinate {cont}: {bob.position()}\n")
        
def main():
    amnesia = 60
    bobLista = []

    bob = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(500, 500)
    bob.penup()

    file = open("BobFile.csv", "w") 

    for cont in range(amnesia)
        scelta = random.randint(1, 4) #Scelta randomica tra 1 e 4
        bobLista.append(scelta)

    percorso(bobLista, amnesia, bob, file)

if __name__ == "__main__":
    main()