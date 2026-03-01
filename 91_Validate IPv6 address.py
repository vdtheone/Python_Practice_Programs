# Validate IPv6 address

import re

def is_valid_ipv6(ip):
    pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return re.match(pattern, ip) is not None 

# Example usage
ip_address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
if is_valid_ipv6(ip_address):
    print(f"{ip_address} is a valid IPv6 address.")
else:    
    print(f"{ip_address} is not a valid IPv6 address.")

ip_address = "2001:0db8:85a3:0000:0000:8a2e:0370:733g"
if is_valid_ipv6(ip_address):    
    print(f"{ip_address} is a valid IPv6 address.")
else:    
    print(f"{ip_address} is not a valid IPv6 address.")    