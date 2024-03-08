#Classe testo che quando viene istanziato permette di contenere un testo in chiaro oppure codificato che avrà il testo, la chiave ed un booleano per vedere se è in chiaro 
#oppure codificato. Avrà come metodi cifra e decifra. 

class Testo():
    def __init__(self, stringa, chiave, cifrato):
        # Inizializza gli attributi dell'oggetto
        self.stringa = stringa.lower()  # Converte la stringa in minuscolo
        self.chiave = chiave.lower()  # Converte la chiave in minuscolo
        self.cifrato = cifrato  # Indica se la stringa è cifrata o meno (True/False)
        self.cifra = []  # Lista che conterrà i risultati della cifratura
        self.decifra = []  # Lista che conterrà i risultati della decifratura
        
    def cifra_cod(self, dizio):
        if not self.cifrato:  # Se la stringa non è ancora cifrata
            lista_chiave = [c for c in self.chiave]  # Crea una lista con i caratteri della chiave
            for indice, char in enumerate(self.stringa):
                # Cifra ogni carattere sommando i corrispondenti numeri della chiave e della stringa
                self.cifra.append((dizio[char] + dizio[lista_chiave[indice]]) % 21)
            
            self.cifrato = True  # Imposta il flag cifrato a True
            print(",".join(str(c) for c in self.cifra))  # Stampa la stringa cifrata separando i numeri con virgola
        else:
            print("La stringa è già cifrata")
    
    def decifra_cod(self, dizio, diz_num):
        if self.cifrato:  # Se la stringa è cifrata
            lista_chiave = [c for c in self.chiave]  # Crea una lista con i caratteri della chiave
            for indice, elem in enumerate(self.cifra):
                # Decifra ogni elemento sottraendo i corrispondenti numeri della chiave e della stringa
                self.decifra.append(dizio[(elem - diz_num[lista_chiave[indice]]) % 21])
            
            self.cifrato = False  # Imposta il flag cifrato a False
            print("".join(c for c in self.decifra))  # Stampa la stringa decifrata (senza virgole)

        else:
            print("La stringa è già decifrata")

def main():
    # Dizionario che mappa numeri a lettere
    diz_par = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f',
               6: 'g', 7: 'h', 8: 'i', 9: 'l', 10: 'm', 11: 'n', 12: 'o',
               13: 'p', 14: 'q', 15: 'r', 16: 's', 17: 't', 18: 'u', 19: 'v', 20: 'z'}

    # Dizionario inverso che mappa lettere a numeri
    diz_num = {v: k for k, v in diz_par.items()}

    # Chiede all'utente di inserire una parola
    parola = input("Inserisci una parola: ")

    # Crea un oggetto Testo con la parola inserita, la chiave "abcdefghijkl" e il flag cifrato impostato su False
    testo = Testo(parola, "abcdefghijkl", False)

    # Cifra la parola
    testo.cifra_cod(diz_num)

    # Decifra la parola cifrata
    testo.decifra_cod(diz_par, diz_num)

if __name__ == "__main__":
    main()


    #diz_num = {} #Per convertire la chiave in oggetto e viceversa
    #for cifra in dizLetNum:
    #    dizNumLet[dizLetNum[chiave]] = chiave