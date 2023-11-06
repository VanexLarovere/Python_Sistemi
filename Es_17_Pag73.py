import math

def main():
    num = int(input("Inserisci un numero: "))
    esponente = int(math.log2(num))

    lista = [2**i for i in range(0, esponente + 1) if (2**i <= num)] #Ciclo e prendo solo quelli che sono <= di num

    print(lista)

if __name__ == "__main__":
    main()