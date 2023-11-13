#Scrivi un programma python che permetta all'utente di inserire due numeri. 
#Crea una lista contenente: La somma dei quadrati dei due numeri, il quadrato della somma dei numeri, 
#la differenza tra i quadrati dei due numeri, il quadrato della differenza tra i due numeri. 
#Stampa poi  la lista ottenuta


def main():
    n1 = float(input("Inserisci il primo numero: "))
    n2 = float(input("Inserisci il secondo numero: "))

    somma_quadrati = n1**2 + n2**2 #** vuol dire potenza
    quadrato_somma = (n1 + n2)**2
    differenza_quadrati = n1**2 - n2**2
    quadrato_differenza = (n1 - n2)**2

    risultati = [somma_quadrati, quadrato_somma, differenza_quadrati, quadrato_differenza]

    print(f"Lista ottenuta: {risultati}")

if __name__ == "__main__":
    main()