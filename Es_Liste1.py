#<LE LISTE>
#Qualcosa simile ai vettori di C
def print_list(l):
    print("La lista e' :", end=" ")
    for elemento in l:
        print(elemento, end = " ") #end serve per mettere qualcosa tra gli elementi, in questo caso uno spazio
    print("\n")

def main():
    l = [1, 2, 3, 4, "c", 3.14, "python"] #Posso fare liste con tipi diversi
    r = [10, 11, 12]
    print(l)
    print(l[-1])
    print_list(l[::-1])
    print_list(l+r) #Concatena l ed r
    print_list(3*r) #Concatena r 3 volte

    #chiediamo all'utente una lista e la memorizziamo
    lista = [] #Creo la lista vuota
    num = 1 #Così entra dentro il while
    while num>0:
        num = int(input("Scrivi un numero: (-1 per interrompere): "))
        if num>0:
            lista.append(num) #aggiungo a lista num  
    print_list(lista)


if __name__ == "__main__":
    main()