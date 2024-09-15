import os,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.subnetting import calculate_subnet_from_cidr, calculate_subnet_from_ip_and_mask, calculate_subnets, display_subnet_info, show_subnet_details
import ipaddress
import os


def test_calculate_subnet_from_cidr():
    print("\nTesting calculate_subnet_from_cidr")
    cidr = "192.168.1.0/24"
    result = calculate_subnet_from_cidr(cidr)
    print(result)

def test_calculate_subnet_from_ip_and_mask():
    print("\nTesting calculate_subnet_from_ip_and_mask")
    ip = "192.168.1.10"
    subnet_mask = "255.255.255.0"
    result = calculate_subnet_from_ip_and_mask(ip, subnet_mask)
    print(result)

def test_calculate_subnets():
    print("\nTesting calculate_subnets")
    ip = "192.168.1.0"
    num_subnets = 4
    result = calculate_subnets(ip, num_subnets)
    for subnet in result:
        print(f"Subnet {subnet['Subnet']}:")
        print(f"  Network Address: {subnet['Network Address']}")
        print(f"  Subnet Mask: {subnet['Subnet Mask']}")
        print(f"  Broadcast Address: {subnet['Broadcast Address']}")
        print(f"  Gateway (primo host): {subnet['Gateway (primo host)']}")
        print(f"  Last Usable Host: {subnet['Last Usable Host']}")
        print(f"  Total Usable Hosts: {subnet['Total Usable Hosts']}")
        print("  All IPs (primi 10):")
        for ip in subnet['All IPs']:
            print(f"    {ip}")
        print()

def test_display_subnet_info():
    print("\nTesting display_subnet_info")
    subnets = [
        {
            "Subnet": 1,
            "Network Address": ipaddress.IPv4Address("192.168.1.0"),
            "Subnet Mask": ipaddress.IPv4Network("192.168.1.0/26").netmask,
            "Broadcast Address": ipaddress.IPv4Address("192.168.1.63"),
            "Gateway (primo host)": ipaddress.IPv4Address("192.168.1.1"),
            "Last Usable Host": ipaddress.IPv4Address("192.168.1.62"),
            "Total Usable Hosts": 62,
            "All IPs": [ipaddress.IPv4Address("192.168.1.1")]
        }
    ]
    display_subnet_info(subnets)

def test_show_subnet_details():
    print("\nTesting show_subnet_details")
    subnet = {
        "Subnet": 1,
        "Network Address": ipaddress.IPv4Address("192.168.1.0"),
        "Subnet Mask": ipaddress.IPv4Network("192.168.1.0/26").netmask,
        "Broadcast Address": ipaddress.IPv4Address("192.168.1.63"),
        "Gateway (primo host)": ipaddress.IPv4Address("192.168.1.1"),
        "Last Usable Host": ipaddress.IPv4Address("192.168.1.62"),
        "All IPs": [ipaddress.IPv4Address("192.168.1.1")]
    }
    show_subnet_details(subnet)

if __name__ == "__main__":
    test_calculate_subnet_from_cidr()
    test_calculate_subnet_from_ip_and_mask()
    test_calculate_subnets()
    test_display_subnet_info()
    test_show_subnet_details()
