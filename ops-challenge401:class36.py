#!/bin/usr/python3

# Script Name:                      401 ops challenge 36
# Author:                           Ethan Pham
# Date of latest revision:          Jun 17, 2024
# Purpose:                          Create a script that performs banner grabbing

import subprocess

def main():
    target = input("Enter the URL or IP address of target: ")

    port = input("Enter the port number: ")

    print("\n[+] Banner grabbing using netcat:")
    try:
        netcat_result = subprocess.check_output(['nc', '-v', '-n', '-z', '-w 1', target, port], stderr=subprocess.STDOUT, universal_newlines=True)
        print(netcat_result)
    except subprocess.CalledProcessError as e:
        print(f"Error executing netcat: {e.output}")

    print("\n[+] Banner grabbing using telnet:")
    try:
        telnet_result = subprocess.check_output(['telnet', target, port], stderr=subprocess.STDOUT, universal_newlines=True)
        print(telnet_result)
    except subprocess.CalledProcessError as e:
        print(f"Error executing telnet: {e.output}")

    print("\n[+] Banner grabbing using Nmap on well-known ports:")
    try:
        nmap_result = subprocess.check_output(['nmap', '-sV', '-p', '1-1023', target], stderr=subprocess.STDOUT, universal_newlines=True)
        print(nmap_result)
    except subprocess.CalledProcessError as e:
        print(f"Error executing Nmap: {e.output}")

if __name__ == "__main__":
    main()