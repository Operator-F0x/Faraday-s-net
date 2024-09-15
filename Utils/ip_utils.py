def ip_to_binary(ip):
    """Convert an IP address (IPv4Address or string) to a binary string."""
    try:
        ip_str = str(ip)
        return '.'.join(format(int(octet), '08b') for octet in ip_str.split('.'))
    except ValueError:
        print(f"Error: Invalid IP {ip}")
        return None
