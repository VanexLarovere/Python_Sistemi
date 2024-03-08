#Lambda Function, utile x definire funzioni brevi
def main():
    somma = lambda x, y: x + y
    maggMin = lambda x, y: x < y

    x, y = 10, 4
    print(somma(x, y))
    print(maggMin(x, y))

    #############################
    lista = [10, 4]
    print(somma(*lista)) #Stessa cosa di scrivere print(somma(lista[0], lista[1]))

if __name__ == "__main__":
    main()