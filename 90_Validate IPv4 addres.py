# Validate IPv4 addres

import re

def is_valid_ipv4(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

# Example usage
ip_address = "192.168.1.1"
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")

ip_address = "256.256.256.256"
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:    
    print(f"{ip_address} is not a valid IPv4 address.")    