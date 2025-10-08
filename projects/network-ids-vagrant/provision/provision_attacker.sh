#!/usr/bin/env bash
set -e

apt-get update -y
DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip nmap
pip3 install scapy

# Ensure vagrant user owns home
chown -R vagrant:vagrant /home/vagrant
