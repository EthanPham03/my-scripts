#!/bin/usr/python3

# Script Name:                      401 ops challenge 12
# Author:                           Ethan Pham
# Date of latest revision:          May 14, 2024
# Purpose:                          Add an ICMP Ping Sweep tool and a user menu 

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

def icmp_ping_sweep(network):
    hosts_online = 0
    for host in ipaddress.IPv4Network(network).hosts():
        host = str(host)
        if host != network.network_address and host != network.broadcast_address:
            response = scapy.sr1(scapy.IP(dst=host)/scapy.ICMP(), timeout=1, verbose=False)
            if response is None:
                print(f"Host is unresponsive.")
            elif response.haslayer(scapy.ICMP):
                if response[scapy.ICMP].type == 3 and response[scapy.ICMP].code in [1, 2, 3, 9, 10, 13]:
                    print(f"Host is actively blocking ICMP traffic.")
                else:
                    print(f"Host is responding.")
                    hosts_online += 1
    print(f"Total hosts online: {hosts_online}")

def menu():
    print("Select an option:")
    print("1. TCP Port Range Scanner mode")
    print("2. ICMP Ping Sweep mode")
    choice = input("Enter your choice: ")
    return int(choice)

if __name__ == "__main__":
    choice = menu()
    if choice == 1:
        host = "192.168.0.1"
        port_range = range(1, 100)
        tcp_port_scan(host, port_range)
    elif choice == 2:
        network_address = input("Enter network address: ")
        network = ipaddress.IPv4Network(network_address)
        icmp_ping_sweep(network)
    else:
        print("Invalid choice")