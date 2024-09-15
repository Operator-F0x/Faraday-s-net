import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Subnetting.SubneTools import calculate_subnet_from_cidr,calculate_subnets,ip_to_binary

if __name__ == "__main__":

    ip = "192.168.1.1"
    subnetmask = "255.255.255.0"
    num_subnet = 12
    cidr = "192.168.1.1/24"

    subnet_info = calculate_subnet_from_cidr(cidr)
    print(f"\nNetwork Address: {subnet_info['Network Address']}")
    print(f"Broadcast Address: {subnet_info['Broadcast Address']}")
    print(f"Usable Hosts Range: {subnet_info['Usable Hosts Range'][0]} to {subnet_info['Usable Hosts Range'][1]}")

    binaryip = ip_to_binary(ip)
    print(f"\nip to Binary output\n{ip}\n{binaryip}")