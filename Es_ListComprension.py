#LIST COMPREHENSION
#Lista con i primi 5 quadrati perfetti
import random

quadrati = (i**2 for i in range(1, 6)) #i**2 è una potenza, in range 1-6 6 escluso
print(quadrati)

numeri_interi = (i for i in range(1, 11)) #in range = nell'intervallo 1-10 (11 escluso)
print(numeri_interi)

#lista con solo le parole che iniziano con c
stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = (parola for parola in stringhe if parola[0]=="c")
print(stringhe_c)

#Mette random tutti i voti + scrive solo i voti insufficienti
voti = (random.randint(2, 10) for l in range (0, 10))
print(voti)
voti_insuff = (voti for voti in voti if voto<6)
print(voti_insuff)