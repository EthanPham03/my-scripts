#!/bin/usr/python3

# Script Name:                      401 ops challenge 11
# Author:                           Ethan Pham
# Date of latest revision:          May 13, 2024
# Purpose:                          Create a TCP Port Range Scanner that tests whether a TCP port is open or closed

from scapy.all import

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

if __name__ == "__main__":
    host = "8.8.8.8"
    port_range = range(1, 100)
    port_scan(host, port_range)