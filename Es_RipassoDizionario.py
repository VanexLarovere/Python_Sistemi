dizionario = {"a":"albero", "b":"brutto", "c":"casa"}
lista = ["albero", "brutto", "casa"]

print(dizionario["b"]) #La chiave la possiamo scegliere noi
print(lista[1])

dizionario["d"] = "dado"
print(dizionario)

dizionario["a"] = "alto"
print(dizionario["a"]) #Scriverà alto perché lo sovvrascrive

for chiave in dizionario: #Ciclo sul dizionario
    print(f"La chiave {chiave} ha valore: {dizionario[chiave]}")

