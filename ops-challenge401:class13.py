#!/bin/usr/python3

# Script Name:                      401 ops challenge 13
# Author:                           Ethan Pham
# Date of latest revision:          May 15, 2024
# Purpose:                          Add a feature that pings an IP address and scans its ports for openings

import subprocess
subprocess.check_call(["pip", "install", "scapy"])
import scapy.all as scapy
import ipaddress

def port_scan(host, port_range):
    for port in port_range:
        response = sr1(IP(dst=host)/TCP(dport=port, flags="S"), timeout=1, verbose=False)
        if response is not None:
            if response.haslayer(TCP):
                if response[TCP].flags == 0x12:
                    print(f"Port is open")
                    send(IP(dst=host)/TCP(dport=port, flags="R"), verbose=False)
                elif response[TCP].flags == 0x14:
                    print(f"Port is closed")

def icmp_ping(host):
   response = scapy.sr1(scapy.IP(dst=host)/scapy.ICMP(), timeout=1, verbose=False)
    if response is None:
        print(f"Host is unresponsive.")
    elif response.haslayer(scapy.ICMP):
        if response[scapy.ICMP].type == 0:
            print(f"Host is responding.")
            return True
        elif response[scapy.ICMP].type == 3 and response[scapy.ICMP].code in [1, 2, 3, 9, 10, 13]:
            print(f"Host is actively blocking ICMP traffic.")
        else:
            print(f"Host is unresponsive.")

def menu():
    print("Select an option:")
    print("1. Ping and Port Scan mode")
    choice = input("Enter your choice: ")
    return int(choice)

if __name__ == "__main__":
    choice = menu()
    if choice == 1:
        host = input("Enter IP address: ")
        if icmp_ping(host):
            port_range = range(1,100)
            port_scan(host, port_range)
        else:
            print("Invalid choice")