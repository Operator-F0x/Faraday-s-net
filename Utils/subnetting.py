import ipaddress
import math
from .ip_utils import ip_to_binary

def calculate_subnet_from_cidr(cidr: str):
    """Calculate the network address, broadcast address, and usable hosts range from a CIDR."""
    try:
        # Create a network object using the CIDR
        network = ipaddress.IPv4Network(cidr, strict=False)
        
        # Calculate the network address, broadcast address, and usable host range
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        usable_hosts = list(network.hosts())

        if not usable_hosts:
            raise ValueError("The network has no usable hosts.")
        
        # Return results
        return {
            "Network Address": network_address,
            "Broadcast Address": broadcast_address,
            "Usable Hosts Range": (usable_hosts[0], usable_hosts[-1])
        }

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Generic error: {e}")


def calculate_subnet_from_ip_and_mask(ip: str, subnet_mask: str):
    """Calculate the network address, broadcast address, and usable hosts based on an IP and subnet mask."""
    try:
        # Create a network object using the provided IP and subnet mask
        network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
        
        # Calculate the network address, broadcast address, and usable host range
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        usable_hosts = list(network.hosts())

        if not usable_hosts:
            raise ValueError("The network has no usable hosts.")

        # Return results
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
    """Calculate subnets for a given IP and number of subnets."""
    try:
        # Convert the IP to an IPv4Network object with a default network mask (e.g., /24)
        network = ipaddress.IPv4Network(f"{ip}/24", strict=False)

        # Calculate the number of bits needed for the desired number of subnets
        subnet_bits = math.ceil(math.log2(num_subnets))

        # Find the new subnet mask by adding subnet bits to the original prefix
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
                "Gateway (primo host)": usable_hosts[0] if usable_hosts else None,
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
    """Display detailed information for each subnet."""
    if not subnets:
        print("No subnets to display.")
        return

    for info in subnets:
        print(f"Subnet {info['Subnet']}:")
        print(f"  Network Address: {info['Network Address']}")
        print(f"  Subnet Mask: {info['Subnet Mask']}")
        print(f"  Broadcast Address: {info['Broadcast Address']}")
        print(f"  Gateway (primo host): {info['Gateway (primo host)']}")
        print(f"  Last Usable Host: {info['Last Usable Host']}")
        print(f"  Total Usable Hosts: {info['Total Usable Hosts']}")
        print("  All IPs (first 10):")
        for ip in info['All IPs']:
            print(f"    {ip}")
        print()


def show_subnet_details(subnet):
    """Display details of a subnet, including IP addresses in binary format."""
    try:
        print(f"Details for Subnet {subnet['Subnet']}:")
        print(f"  Network Address: {subnet['Network Address']}")
        print(f"  Network Address (Binary): {ip_to_binary(subnet['Network Address'])}")
        print(f"  Subnet Mask: {subnet['Subnet Mask']}")
        print(f"  Subnet Mask (Binary): {ip_to_binary(subnet['Subnet Mask'])}")
        print(f"  Broadcast Address: {subnet['Broadcast Address']}")
        print(f"  Broadcast Address (Binary): {ip_to_binary(subnet['Broadcast Address'])}")
        print(f"  Gateway (primo host): {subnet['Gateway (primo host)']}")
        print(f"  Gateway (primo host) (Binary): {ip_to_binary(subnet['Gateway (primo host)'])}")
        print(f"  Last Usable Host: {subnet['Last Usable Host']}")
        print(f"  Last Usable Host (Binary): {ip_to_binary(subnet['Last Usable Host'])}")
        print("\n  All IPs in this subnet (limited to 10):")
        for ip in subnet['All IPs']:
            print(f"    IP Address: {ip}")
            print(f"    IP Address (Binary): {ip_to_binary(ip)}")
        print()

    except KeyError as ke:
        print(f"Missing key error: {ke}")
    except Exception as e:
        print(f"Generic error: {e}")
