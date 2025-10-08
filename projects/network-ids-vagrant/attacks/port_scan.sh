#!/usr/bin/env bash
# simple nmap scan from attacker to victim
TARGET=192.168.20.10
nmap -p 1-200 $TARGET
