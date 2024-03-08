#Un braccio robotico industriale libero di muoversi avanti e indietro lungo una rotaia è impazzito. 
#Ogni secondo si muove scegliendo a caso tra due possibili movimenti: 1 cm in avanti, oppure 1 cm indietro. 
#Non è possibile togliere corrente al robot senza bloccare tutto lo stabilimento, quindi bisogna attendere lo spegnimento che si 
#effettua tutti i fine settimana e oggi purtroppo è lunedì! Il tuo responsabile ti chiede di creare un programma 
#in Python per simulare lo spostamento totale che il robot avrà effettuato dopo 5 interi giorni di pazzia.

#Definisci una funzione che restituisca uno spostamento casuale (+1 o -1).
#Utilizza una list comprehension per creare la  lista contenente tutta la sequenza degli spostamenti casuali.
#Infine calcola la somma degli spostamenti casuali per ottenere lo spostamento complessivo accumulato in 5 giorni.
import random

def main():
    def listaMovimenti():
        return random.choice(['+1', '-1'])

    n_sec = 60 * 60 * 24 * 5
    n_movim = 0
    lista = []
    somma_mov = 0

    for k in range(n_sec):
        lista.append(int(listaMovimenti()))
        n_movim += 1
        somma_mov += lista[k]

    print(lista)
    print(f"Movimenti: {n_movim} ; Somma Movimenti: {somma_mov}")
if __name__ == "__main__":
    main()

#Parametri con valori di default, servono quando richiamo la stessa funzione con stessi parametri e li cambio poche volte. Do quindi
#come valore di default -2 e +2 (es) e non li includo più nelle funzioni richiamanti (Passerò solo quando ci servirà altri parametri)