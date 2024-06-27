#!/usr/bin/python3

# Script Name:                      401 ops challenge 43
# Author:                           Ethan Pham
# Date of latest revision:          Jun 26, 2024
# Purpose:                          Copy the demo script and complete the objectives. 

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5
sockmod.settimeout(timeout)

hostip = input("Enter host IP: ")
portno = int(input("Enter port number: "))

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)):
        print("Port closed")
    else:
        print("Port open")

portScanner(port)