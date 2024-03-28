#!/bin/bash

# Script Name:                  ops301-challenge03-Conditionals in Menu Systems
# Author:                       Ethan Pham
# Date of latest revision:      03/28/2024
# Purpose:                      Create a script that will use conditionals and loops to execute requests

# Declaration of variables

# Declaration of functions

display_menu() {
    echo "Please select the following options: "
    echo "Hello world"
    echo "Ping self"
    echo "IP info"
    echo "Exit"
}

if [ "$choice" = "Hello world" ]; then
    echo "Hello world!"
elif [ "$choice" = "Ping self" ]; then
    ping -c 4 127.0.0.1 
elif [ "$choice" = "IP info" ]; then
    ip addr show
elif [ "$choice" = "Exit" ]; then
    exit 

# Main
main() {
    while true; do 
        display_menu
        handle_option
        echo ""
    done
}

# End