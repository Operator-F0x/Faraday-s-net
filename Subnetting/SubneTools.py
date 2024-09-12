import ipaddress
import math

def calculate_subnet_from_cidr(cidr:str):
    # Creare un oggetto network utilizzando il CIDR
    network = ipaddress.IPv4Network(cidr, strict=False)
    
    # Calcolare l'indirizzo di rete, l'indirizzo di broadcast e il range degli host
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    usable_hosts = list(network.hosts())
    
    # Risultati
    return {
        "Network Address": network_address,
        "Broadcast Address": broadcast_address,
        "Usable Hosts Range": (usable_hosts[0], usable_hosts[-1])
    }



def calculate_subnets(ip: str, num_subnets: int):
    # Converti l'IP in un oggetto IPv4Network con una maschera di rete predefinita (e.g., /24 o /16)
    network = ipaddress.IPv4Network(f"{ip}/24", strict=False)

    # Calcola quanti bit sono necessari per il numero di sottoreti richieste
    subnet_bits = math.ceil(math.log2(num_subnets))

    # Trova la nuova subnet mask aggiungendo i bit delle sottoreti al prefisso originale
    new_prefix = network.prefixlen + subnet_bits

    # Crea la nuova rete con il prefisso calcolato
    subnets = list(network.subnets(prefixlen_diff=subnet_bits))

    result = []

    for i, subnet in enumerate(subnets[:num_subnets]):
        network_address = subnet.network_address
        broadcast_address = subnet.broadcast_address
        usable_hosts = list(subnet.hosts())

        # Aggiungi le informazioni della sottorete
        result.append({
            "Subnet": i + 1,
            "Network Address": network_address,
            "Subnet Mask": subnet.netmask,
            "Broadcast Address": broadcast_address,
            "Gateway (primo host)": usable_hosts[0] if usable_hosts else None,
            "Last Usable Host": usable_hosts[-1] if usable_hosts else None,
            "Total Usable Hosts": len(usable_hosts)
        })

    return result


def display_subnet_info(subnets):
    """Mostra le informazioni dettagliate per ciascuna sottorete."""
    for info in subnets:
        print(f"Subnet {info['Subnet']}:")
        print(f"  Network Address: {info['Network Address']}")
        print(f"  Subnet Mask: {info['Subnet Mask']}")
        print(f"  Broadcast Address: {info['Broadcast Address']}")
        print(f"  Gateway (primo host): {info['Gateway (primo host)']}")
        print(f"  Last Usable Host: {info['Last Usable Host']}")
        print(f"  Total Usable Hosts: {info['Total Usable Hosts']}")
        print()


def ip_to_binary(ip):
    """Converte un indirizzo IP in una stringa binaria."""
    return '.'.join(format(int(octet), '08b') for octet in ip.split('.'))


def save_subnet_details_to_file(subnet, filename):
    """Salva i dettagli della sottorete in un file di testo, inclusi gli IP di tutti gli host."""
    with open(filename, 'w') as file:
        file.write(f"Details for Subnet {subnet['Subnet']}:\n")
        file.write(f"  Network Address: {subnet['Network Address']}\n")
        file.write(f"  Network Address (Binary): {ip_to_binary(str(subnet['Network Address']))}\n")
        file.write(f"  Subnet Mask: {subnet['Subnet Mask']}\n")
        file.write(f"  Subnet Mask (Binary): {ip_to_binary(str(subnet['Subnet Mask']))}\n")
        file.write(f"  Broadcast Address: {subnet['Broadcast Address']}\n")
        file.write(f"  Broadcast Address (Binary): {ip_to_binary(str(subnet['Broadcast Address']))}\n")
        file.write(f"  Gateway (primo host): {subnet['Gateway (primo host)']}\n")
        file.write(f"  Gateway (primo host) (Binary): {ip_to_binary(str(subnet['Gateway (primo host)']))}\n")
        file.write(f"  Last Usable Host: {subnet['Last Usable Host']}\n")
        file.write(f"  Last Usable Host (Binary): {ip_to_binary(str(subnet['Last Usable Host']))}\n")
        file.write("\n")
        
        file.write("All IPs in this subnet (limited to 10):\n")
        for ip in subnet['All IPs']:
            file.write(f"  IP Address: {ip}\n")
            file.write(f"  IP Address (Binary): {ip_to_binary(ip)}\n")
            file.write("\n")

def show_subnet_details(subnet):
    """Mostra e salva i dettagli binari di ogni IP nella sottorete selezionata in un file di testo."""
    filename = f"subnet_{subnet['Subnet']}_details.txt"
    save_subnet_details_to_file(subnet, filename)
    print(f"Details for Subnet {subnet['Subnet']} have been saved to {filename}")
