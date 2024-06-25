#!/usr/bin/python3

# Script Name:                      401 ops challenge 42
# Author:                           Ethan Pham
# Date of latest revision:          Jun 25, 2024
# Purpose:                          Copy the demo script and complete the objectives. 

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""") 
print("You have selected option: ", resp)

range = '1-50'

### TODO: Prompt the user to type in a port range for this tool to scan
port_range = input("Enter the port range: ")
if not port_range:
    port_range = '1-50'

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS -sU -sV -sC -A')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr].all_protocols():
        print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
else:
    print("Please enter a valid option")