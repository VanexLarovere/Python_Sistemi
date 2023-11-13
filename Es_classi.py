class Quadrato(): #Class + nome della classe
    #Costrutture
    def __init__(self, lato): #Tutti i costruttori si chiamano sempre init
        #Attributo
        self.lato = lato #self sarebbe this di java
    def calcolaArea(self): #Tutti i metodi hanno sempre il self + eventuali parametri
        return self.lato**2
    def stampaLato(self):
        print(f"Il lato è {self.lato}")

def main():
    q = Quadrato(4)
    print(f"L'area del quadrato e' {q.calcolaArea()}")
    q.lato = 5
    print(f"L'area del quadrato e' {q.calcolaArea()}")

if __name__ == "__main__":
    main()