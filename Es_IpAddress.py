#Chiedere all'utente un ip address ed una subnet mask. Usando la classe stampare se l'indirizzo è privato, di loopback, 
#oppure se l'indirizzo di rete è valido (se si allora stampa tutti gli ip utili utilizzabili (host))
import ipaddress

n_ip = input("Inserisci un ip address: ")
subnet = input("Inserisci una subnet mask (/n): ")
        
ipv4Pieno = n_ip + subnet
ip = ipaddress.IPv4Address(n_ip)
        
if ip.is_private:
    print("è privato")
if ip.is_loopback:
    print("è loopback")
iprete = ipaddress.IPv4Network(ipv4Pieno, strict = False)
if ipv4Pieno == str(iprete): #Si genera la rete che contiene l'indirizzo, se le rete sono uguali vuol dire che ho inserito un ip di rete
    print(f"è di rete perché l'indirizzo {ipv4Pieno} coincide con {iprete}")
else:
    print(f"Non è di rete perché l'indirizzo {ipv4Pieno} non coincide con {iprete}")
print(f"indirizzo di rete: {iprete}")
hosts = list(iprete.hosts())
print(f"Il primo ip utilizzabile è {hosts[0]}")
print(f"L'ultimo ip utilizzabile è {hosts[-1]}")