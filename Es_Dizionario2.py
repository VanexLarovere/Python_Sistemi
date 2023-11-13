#Da un file di testo rubrica.txt con contatti telefonici (nome1, 359372748). 
#Leggere e caricare in un dizionario (d = 359377384: "nome1", 345783782: "nome2")

#Implementare una ricerca di un numero o un nome

def main():
    rubrica = {}
    file = open("rubrica.txt", "r")
    righe = file.readlines() #Legge tutte le righe

    for riga in righe:
        campi = riga.split(", ") #Ritorna una lista con tutte le parti
        numeroTelefonico = int(campi[1].replace("\n", "")) #Sostituisce il carattere \n con linea vuota (Quindi cancella)
        nome = campi[0]
        rubrica[numeroTelefonico] = nome
    
    print(rubrica)
    file.close()

if __name__ == "__main__":
    main()