#!/bin/bash

# Script Name:                  ops201-challenge02-my-first-bash-script
# Author:                       Ethan Pham
# Date of latest revision:      02/20/2024
# Purpose:                      Create a script that prints a string to the console
#
# Declaration of variables
pstree 
read -p "What is PID" 
kill -9 "What is PID"
 echo $$

pstree=0

# Declaration of functions



# Main

 while [ $pstree -lt 5]

do 
    echo $pstree
    pstree=$((pstree+1))
done
# Use the kill command to terminate the process with the specified PID

# End