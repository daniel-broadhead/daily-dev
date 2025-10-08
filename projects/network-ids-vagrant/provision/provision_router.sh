#!/usr/bin/env bash
set -e

# Update + install
apt-get update -y
DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip tcpdump iproute2 iptables

# Python packages
pip3 install --upgrade pip
pip3 install scapy

# Enable IP forwarding
sysctl -w net.ipv4.ip_forward=1
# Make persistent
grep -q "^net.ipv4.ip_forward=1" /etc/sysctl.conf || echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf

# Allow forwarding in iptables (simple permissive rules for lab)
iptables -A FORWARD -i eth1 -o eth2 -j ACCEPT
iptables -A FORWARD -i eth2 -o eth1 -j ACCEPT

# Optional: NAT if you want outbound to host network (commented out)
# iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Create directory for detector
mkdir -p /home/vagrant/detector
chown -R vagrant:vagrant /home/vagrant/detector
