#Testo: Inizializzare 4 variabili (1 int, 1 stringa, 1 float, 1 bool) e stampare il
#loro valore con il loro tipo usando type()

def main():
    n1 = int(input("Inserisci una variabile intera: "))
    n2 = input("Inserisci una variabile stringa: ") #Si restituisce già una stringa, quindi non c'è il caso di usare il casting
    n3 = float(input("Inserisci una variabile reale: "))
    n4 = bool(input("Inserisci una variabile booleana: "))

    print(f"Valore 1 : {n1}, tipo: {type(n1)}")
    print(f"Valore 2 : {n2}, tipo: {type(n2)}")
    print(f"Valore 3 : {n3}, tipo: {type(n3)}")
    print(f"Valore 4 : {n4}, tipo: {type(n4)}")



if __name__ == "__main__":
    main()