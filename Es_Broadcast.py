import ipaddress

def calcola_subnet_broadcast(indirizzo_ip, cdr):
    # Creare un oggetto di tipo IPv4Network utilizzando l'indirizzo IP e il CDR
    rete = ipaddress.IPv4Network(f"{indirizzo_ip}/{cdr}", strict=False)

    # Ottenere la subnet mask e il broadcast
    subnet_mask = rete.netmask
    broadcast = rete.broadcast_address

    return subnet_mask, broadcast

def main():
    # Input: indirizzo IP e CDR
    indirizzo_ip = input("Inserisci l'indirizzo IP (formato xxx.xxx.xxx.xxx): ")
    cdr = int(input("Inserisci il CDR: "))

    # Calcolare subnet mask e broadcast
    subnet_mask, broadcast = calcola_subnet_broadcast(indirizzo_ip, cdr)

    # Stampare i risultati
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Broadcast: {broadcast}")

if __name__ == "__main__":
    main()
