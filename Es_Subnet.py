def cdr_to_mask(cdr):
    if cdr < 0 or cdr > 32:
        print("La subnet mask deve essere compresa tra 0 e 32")
    mask = (2 ** 32 - 1) - (2 ** (32 - cdr) - 1)
    return mask

# Funzione per calcolare l'indirizzo IP di rete e l'indirizzo IP di broadcast
def calcolo_network_broadcast(ip, subnet_mask):
    network = ip & subnet_mask
    broadcast = ip | subnet_mask
    return network, broadcast

# Richiesta all'utente dell'indirizzo IP e della subnet mask
ip_str = input("Inserisci l'indirizzo IP (esempio: 192.168.1.1): ")
subnet_cdr = int(input("Inserisci la subnet mask in notazione CDR (0-32): "))

def main():
    # Converti l'indirizzo IP in un intero a 32 bit
    ottetti = [int(ottetto) for ottetto in ip_str.split('.')]
    if len(ottetti) != 4 or not all(0 <= ottetto <= 255 for ottetto in ottetti):
        print("Formato dell'indirizzo IP non valido.")
    ip = (ottetti[0] << 24) + (ottetti[1] << 16) + (ottetti[2] << 8) + ottetti[3]

    subnet_mask = cdr_to_mask(subnet_cdr)

    network = calcolo_network_broadcast(ip, subnet_mask)
    broadcast = calcolo_network_broadcast(ip, subnet_mask)

    # Converti l'indirizzo IP di rete e di broadcast in formato decimale puntato
    network_str = ".".join(str((network >> i) & 0xFF) for i in (24, 16, 8, 0))
    broadcast_str = ".".join(str((broadcast >> i) & 0xFF) for i in (24, 16, 8, 0))

    print("Indirizzo IP di rete:", network_str)
    print("Indirizzo IP di broadcast:", broadcast_str)

if __name__ == "__main__":
    main()