#Data la lista ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
#crea un file “mask.txt” in cui salvi le subnet mask associate a ciascun indirizzo IP.

def subnet(group):
    subnetFin = []
    while j < 32:
        subnetFin.append(group[j:j+8] + ".".join(group[j+8]))
        j += 8
    return subnetFin

#with file as open("mask.txt", "w") as file (Togliamo quindi file open e close ed indentiamo tutto), leggerà fino alla fine del contenuto del file

def subnetbinario(indirizzo):
    s = indirizzo[-2:]
    group = ['0'] * 32
    print(s)
    for k in s:
        group[int(k)] = '1'
    return subnet(group)


def main():
    ip_address = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]
    file = open("mask.txt", "w")
    for k in ip_address:
        #ip, subnet = ip_address.split("/") Spezza la lista in 2, la prima parte la assegna a ip, la seconda a subnet
        sub = subnetbinario(ip_address[k])
        print(f"Indirizzo {ip_address[k]}: Subnet: {sub}\n")
        file.write(f"Indirizzo {ip_address[k]}: Subnet: {sub}\n") 
    file.close()


if __name__ == "__main__":
    main()