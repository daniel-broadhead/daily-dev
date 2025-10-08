#!/usr/bin/env bash
set -e

apt-get update -y
DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip iputils-ping
pip3 install scapy

chown -R vagrant:vagrant /home/vagrant
