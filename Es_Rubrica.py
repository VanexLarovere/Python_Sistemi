#Leggere dal file rubrica.txt il numero di telefono e il nome
#salvare in un dizionario come chiave il numero di telefono e come elemento il nome
def cercaNomeInDiz(nomeDaTrovare, rubrica):
    for numTel in rubrica: #in un dizionario si cicla sempre per chiave
        if rubrica[numTel] == nomeDaTrovare:
            return numTel
    return None

def cercaNumTelInDiz(numTelDaTrovare, rubrica):
    if numTelDaTrovare in rubrica:
        return rubrica[numTelDaTrovare]
    else:
        return None

def main():
    d = {}
    file = open("rubrica.txt", "r")
    listaRighe = file.readlines()
    file.close()
    for riga in listaRighe:
        campi = riga.split(", ")#restituisce lista
        nome = campi[0]
        numeroTel = int(campi[1][:-1])
        d[numeroTel] = nome
    nomeDaTrovare = input("inserisci il nome da cercare: ")
    numTelTrovato = cercaNomeInDiz(nomeDaTrovare, d)
    print(f"numero telefono di {nomeDaTrovare} è {numTelTrovato} (se il numero di telefono è 0, non esiste un contatto di nome {nomeDaTrovare})")
    numTelTrovare = int(input("inserisci il numero di telefono da cercare"))
    nomeTrovato = cercaNumTelInDiz(numTelTrovare, d)
    print(f"numero telefono di {nomeTrovato} è {numTelTrovare} ")


if _name_ == "_main_":
    main()