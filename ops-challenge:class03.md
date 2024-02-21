#!/bin/bash

# Script Name:                  ops201-challenge03-functions
# Author:                       Ethan Pham
# Date of latest revision:      02/21/2024
# Purpose:                      Write a function that prints the login history of users on this computer, followed by the text "This is the login istory". In your script, call that function three times.

# Declaration of variables
greeting="ethanpham  ttys000                   Wed Feb 21 17:32   still logged in
ethanpham  ttys000                   Wed Feb 21 17:30 - 17:30  (00:00)
ethanpham  ttys000                   Wed Feb 21 14:57 - 14:57  (00:00)
ethanpham  ttys000                   Tue Feb 20 15:02 - 15:02  (00:00)"
# Declaration of functions
print_message() {
echo $greeting
}


# Main
echo $greeting



# End