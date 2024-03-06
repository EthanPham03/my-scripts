#!/bin/bash

# Script Name:                  ops-challenge13-domain-analyzer
# Author:                       Ethan Pham
# Date of latest revision:      03/06/2024
# Purpose:                      Create a script that asks a user to type

# Declaration of variables



# Declaration of functions

sudo apt-get update
sudo apt-get install whois

echo "Google.com"
read domain

whois $domain
dig $domain
host $domain
nslookup $domain

# Main



# End
