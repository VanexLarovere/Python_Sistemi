a = 1
print(f"il valore di a è {a}")

def main(): #definizione della funzione main
    nome = input("Come ti chiami? ") #Aspetta un input(Ritorna solo stringhe)
    print(f"Il tuo nome è {nome}") #Si usa quando si include una variabile nella frase

    print("Questa è una nuova riga") #In python va sempre a capo senza lo \n

    anni = int(input("Quanti anni hai?")) 
    print(f"Tu hai {anni} anni")

    print(type(anni)) #Usato per sapere il tipo di qualunque variabile di python

    anno_corrente = int(print("In che anno siamo?"))

    print(f"Sei nato nel {anno_corrente-anni}")

if __name__ == "__main__": #Doppio underscore (_)
    main()