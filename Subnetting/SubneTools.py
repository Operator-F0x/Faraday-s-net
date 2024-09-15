import ipaddress
import math

def calculate_subnet_from_cidr(cidr: str):
    """Calculates the network address, broadcast address, and host range from a CIDR."""
    try:
        # Create a network object using the CIDR
        network = ipaddress.IPv4Network(cidr, strict=False)
        
        # Calculate the network address, broadcast address, and host range
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        usable_hosts = list(network.hosts())

        if not usable_hosts:
            raise ValueError("The network has no usable hosts.")
        
        # Results
        return {
            "Network Address": network_address,
            "Broadcast Address": broadcast_address,
            "Usable Hosts Range": (usable_hosts[0], usable_hosts[-1])
        }

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Generic error: {e}")
    

def calculate_subnets(ip: str, num_subnets: int):
    """Calculates the subnets of a given IP based on the desired number of subnets."""
    try:
        # Convert the IP into an IPv4Network object with a default subnet mask (e.g., /24)
        network = ipaddress.IPv4Network(f"{ip}/24", strict=False)

        # Calculate how many bits are needed for the desired number of subnets
        subnet_bits = math.ceil(math.log2(num_subnets))

        # Find the new subnet mask by adding the subnet bits to the original prefix
        new_prefix = network.prefixlen + subnet_bits
        if new_prefix > 32:
            raise ValueError("The number of requested subnets is too large for the provided IP.")
        
        # Create the new network with the calculated prefix
        subnets = list(network.subnets(prefixlen_diff=subnet_bits))

        result = []

        for i, subnet in enumerate(subnets[:num_subnets]):
            network_address = subnet.network_address
            broadcast_address = subnet.broadcast_address
            usable_hosts = list(subnet.hosts())

            result.append({
                "Subnet": i + 1,
                "Network Address": network_address,
                "Subnet Mask": subnet.netmask,
                "Broadcast Address": broadcast_address,
                "Gateway (first host)": usable_hosts[0] if usable_hosts else None,
                "Last Usable Host": usable_hosts[-1] if usable_hosts else None,
                "Total Usable Hosts": len(usable_hosts),
                "All IPs": usable_hosts[:10]  # Show only the first 10 IPs for convenience
            })

        return result

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Generic error: {e}")


def display_subnet_info(subnets):
    """Displays detailed information for each subnet."""
    if not subnets:
        print("No subnets to display.")
        return

    for info in subnets:
        print(f"Subnet {info['Subnet']}:")
        print(f"  Network Address: {info['Network Address']}")
        print(f"  Subnet Mask: {info['Subnet Mask']}")
        print(f"  Broadcast Address: {info['Broadcast Address']}")
        print(f"  Gateway (first host): {info['Gateway (first host)']}")
        print(f"  Last Usable Host: {info['Last Usable Host']}")
        print(f"  Total Usable Hosts: {info['Total Usable Hosts']}")
        print("  All IPs (first 10):")
        for ip in info['All IPs']:
            print(f"    {ip}")
        print()


def ip_to_binary(ip):
    """Converts an IP address (IPv4Address or string) into a binary string."""
    try:
        ip_str = str(ip)
        return '.'.join(format(int(octet), '08b') for octet in ip_str.split('.'))
    except ValueError:
        print(f"Error: Invalid IP {ip}")
        return None


def show_subnet_details(subnet):
    """Displays the details of a subnet, including IP addresses in binary format."""
    try:
        print(f"Details for Subnet {subnet['Subnet']}:")
        print(f"  Network Address: {subnet['Network Address']}")
        print(f"  Network Address (Binary): {ip_to_binary(subnet['Network Address'])}")
        print(f"  Subnet Mask: {subnet['Subnet Mask']}")
        print(f"  Subnet Mask (Binary): {ip_to_binary(subnet['Subnet Mask'])}")
        print(f"  Broadcast Address: {subnet['Broadcast Address']}")
        print(f"  Broadcast Address (Binary): {ip_to_binary(subnet['Broadcast Address'])}")
        print(f"  Gateway (first host): {subnet['Gateway (first host)']}")
        print(f"  Gateway (first host) (Binary): {ip_to_binary(subnet['Gateway (first host)'])}")
        print(f"  Last Usable Host: {subnet['Last Usable Host']}")
        print(f"  Last Usable Host (Binary): {ip_to_binary(subnet['Last Usable Host'])}")
        print("\n  All IPs in this subnet (limited to 10):")
        for ip in subnet['All IPs']:
            print(f"    IP Address: {ip}")
            print(f"    IP Address (Binary): {ip_to_binary(ip)}")
        print()

    except KeyError as ke:
        print(f"Error: Missing key {ke}")
    except Exception as e:
        print(f"Generic error: {e}")
