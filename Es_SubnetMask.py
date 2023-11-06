def completa_8bit(bits):
    return '0' * (8 - len(bits)) + bits

def main():
    n = int(input("Inserisci un numero intero compreso tra 1 e 31: "))
    if n < 1 or n > 31:
        print("Numero non valido")
    else:
        group = ['0'] * 32 #Inizializzo a 0 32 bit
        for k in range(n): #Metto solo n numeri a 1
            group[k] = '1'

        j = 0
        while j < 32: 
            print(int(completa_8bit(''.join(group[j:j+8])), 2)) #Stampo in intero 
            j += 8

if __name__ == "__main__":
    main()