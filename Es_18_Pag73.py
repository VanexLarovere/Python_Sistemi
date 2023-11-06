import math

def main():
    #lista = [i**2 for i in range(0, int.math.sqrt(200) +1) if(i % 2 != 0) and (i**2 < 200)] una soluzione + ottimale
    lista = [i**2 for i in range(0, 1000) if(i % 2 != 0) and (i**2 < 200)] #Questa è una list comprension
    print(f"Quadrati perfetti dispari: {lista}")

if __name__ == "__main__":
    main()