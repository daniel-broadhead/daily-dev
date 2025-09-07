import subprocess
import ipaddress
import socket

subnet = '192.168.1.0/24'

print("Scanning subnet:", subnet)
for ip in ipaddress.IPv4Network(subnet):
    ip_str = str(ip)
    try:
        # Ping the device first
        ping_args = ["ping", "-n", "1", "-w", "1000", ip_str]  # Windows
        result = subprocess.run(ping_args, stdout=subprocess.DEVNULL)
        
        if result.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip_str)[0]
            except socket.herror:
                hostname = "Unknown"
            print(f"{ip_str} is alive, hostname: {hostname}")
    except Exception as e:
        print(f"Error scanning {ip_str}: {e}")
