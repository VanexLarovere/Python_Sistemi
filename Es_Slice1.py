#SLICING DI STRINGHE
s = "ciao come stai?" #Indice 0-1-2-3, in python l'indice è con i numeri negativi (L'ultimo è sempre -1): -4 -3 -2 -1
print(f"1° Modo: Il primo carattere e' {s[0]}")
print(f"2° Modo: l'ultimo carattere e' {s[-1]}") 
print(f"Il penultimo carattere e' {s[-2]}")
print(f"L'ultimo carattere e' {s[len(s)-1]}") #C style

print(s[3:7]) #Dal carattere 3 al carattere 7 escluso
print(s[1:-1]) #Tutti i caratteri tranne il primo e l'ultimo
print(s[1:]) #Stampa dal carattere 1 compreso in poi
print(s[:-1]) #Stampa tutto tranne l'ultimo carattere
print(s[::-1]) #Stampa la stringa all'incontrario partendo dalla fine verso l'inizio