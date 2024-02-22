#!/bin/bash

# Script Name:                  ops201-challenge03-functions
# Author:                       Ethan Pham
# Date of latest revision:      02/21/2024
# Purpose:                      Write a function that prints the login history of users on this computer, followed by the text "This is the login istory". In your script, call that function three times.

# Declaration of variables
echo "$login_history"
login_history=$(last)

# Declaration of functions
print_message () {
    echo "$login_history" 
}

print_message
print_message
print_message
#Call the function
print_message

# Main



# End