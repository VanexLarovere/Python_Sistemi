#Chiedere un numero n dispari da tastiera, si deve stampare un rombo di asterischi con altezza 
#e larghezzza n

def rombo(num):
    spazio = " "
    ast = 1
    
    for i in range(1, num+1, 2):
        print((spazio * ((num - i) // 2)) + ("*" * i))
    
    for i in range(num-2, 0, -2):
        print((spazio * ((num - i) // 2)) + ("*" * i))

def main():
    num = 0
    while num % 2 == 0:
        num = int(input("Inserisci un numero dispari: "))
    
    rombo(num)

if __name__ == "__main__":
    main()
