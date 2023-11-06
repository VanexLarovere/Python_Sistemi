def main():
    max = 10
    power = [[k * i for i in range(1, max +1)] for k in range(1, max +1)]

    for k, tabellina in enumerate(power): #Ritorna indice ed elemento
        #Tabellina è una lista, power è una lista di liste
        print(f"Tabellina del {k + 1}: {tabellina}") #Per rendere più leggibile l'output
        
    file = open("Es_20_Pag73.txt", "w") #Apro file in scrittura

    for tabellina in power:
        file.write(f"{tabellina}\n")

    file.close() #Chiudo il file

if __name__ == "__main__":
    main()