import ipaddress

print("---")
for num, ip in enumerate(ipaddress.IPv4Network('192.168.2.0/23')):
    print(f"R{num}:")
    print("    username: john")
    print("    password: cisco")
    print(f"    hostname: {ip}")
    print("    platform: 'ios'")
    print("    groups:")
    print("      - cisco_group")
    print("\n")
