#!/bin/bash

# Script Name:                  ops201-challenge05-loops
# Author:                       Ethan Pham
# Date of latest revision:      02/23/2024
# Purpose:                      Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.
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