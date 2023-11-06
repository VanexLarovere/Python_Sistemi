import turtle

def main():
    n = (int(input("Inserisci il numero dei lati (intero)")))

    finestra = turtle.Screen()
    rebecca = turtle.Turtle()

    for i in range(0, n):
        rebecca.forward(100)
        rebecca.left(360/n)

    finestra.mainloop()

if __name__ == "__main__":
    main()