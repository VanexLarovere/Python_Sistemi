def main():
    num = int(input("Inserisci un numero: "))
    div = 3
    if num % div == 0:
        print(f"{num} è divisibile per {div}")
    else:
        print(f"{num} non è divisibile per {div}")

if __name__ == "__main__": #dunder = __
    main()
