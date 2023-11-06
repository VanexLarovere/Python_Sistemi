def main():
    num = int(input("Inserisci il numero: "))
    div1 = 2
    div2 = 3
    div3 = 5
    if num % div1 == 0:
        divfin = div1
    else:
        if num % div2 == 0:
            divfin = div2
        else:
            if num % div3 == 0:
                divfin = div3
            else:
                print(f"{num} non è divisibile ne per {div1} ne per {div2} ne per {div3}")

    print(f"{num} è divisibile per {divfin}")

if __name__ == "__main__":
    main()