def compleat8bit(strbin): #Toglie 0B davanti al vedere nella printf e mette 0 fino a giungere a 8 bit
    b = strbin[2:]
    l = len(b)
    return '0' * (8-l) + b


def main():
    ip_adress = input("Inscerisci l'indirizzo IP: ")

    groups = ip_adress.split(".") #Lo spezzo dove c'è il punto ottenendo una lista di stringhe

    groups = [int (group) for group in groups]#Traduce le stringhe in int

    groups = [bin(group) for group in groups]#Traduce in binario 

    print(compleat8bit(groups[0]))
    groups_strbin = print(compleat8bit(strbin) for strbin in groups)
    print(groups)
    print(".".join(groups_strbin)) 

if __name__ == "__main__":
    main()  

