#!/usr/bin/env python3
# Simple IDS using scapy for ARP spoof and port-scan detection
from scapy.all import sniff, ARP, IP, TCP
from collections import defaultdict
import time
import argparse

class IntrusionDetector:
    def __init__(self):
        self.arp_table = {}
        self.port_scan_log = defaultdict(list)
        self.alerts = []

    def detect_arp_spoof(self, pkt):
        if pkt.haslayer(ARP) and pkt[ARP].op == 2:  # ARP reply
            src_ip = pkt[ARP].psrc
            src_mac = pkt[ARP].hwsrc
            if src_ip in self.arp_table:
                if self.arp_table[src_ip] != src_mac:
                    alert = f"[!] ARP spoof detected: {src_ip} changed from {self.arp_table[src_ip]} to {src_mac}"
                    print(alert)
                    self.alerts.append(alert)
            else:
                self.arp_table[src_ip] = src_mac

    def detect_port_scan(self, pkt):
        if pkt.haslayer(TCP) and pkt.haslayer(IP):
            src = pkt[IP].src
            dst = pkt[IP].dst
            dport = pkt[TCP].dport
            ts = time.time()

            self.port_scan_log[src].append((dst, dport, ts))
            # Keep only recent records (window = 3s)
            window = 3.0
            recent = [p for p in self.port_scan_log[src] if ts - p[2] < window]
            self.port_scan_log[src] = recent

            ports_seen = {p[1] for p in recent if p[0] == dst}
            # threshold: > 10 unique dst ports within window
            if len(ports_seen) > 10:
                alert = f"[!] Possible port scan from {src} targeting {dst} (ports: {sorted(list(ports_seen))[:10]} ...)"
                print(alert)
                self.alerts.append(alert)
                # clear to avoid repeated alerts
                self.port_scan_log[src] = []

    def process_packet(self, pkt):
        try:
            self.detect_arp_spoof(pkt)
            self.detect_port_scan(pkt)
        except Exception as e:
            # keep running on parsing errors
            print("[!] Packet processing error:", e)

    def start(self, iface="any"):
        print(f"[*] Starting IDS on interface: {iface} (requires root). Ctrl-C to stop.")
        sniff(iface=iface, prn=self.process_packet, store=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple scapy IDS (ARP spoof + port scan)")
    parser.add_argument("-i", "--iface", default="any", help="Interface to sniff (default: any)")
    args = parser.parse_args()

    ids = IntrusionDetector()
    ids.start(iface=args.iface)
