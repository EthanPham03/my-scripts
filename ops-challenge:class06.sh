#!/bin/bash

# Script Name:                  ops201-challenge02-my-first-bash-script
# Author:                       Ethan Pham
# Date of latest revision:      02/20/2024
# Purpose:                      Create a script that prints a string to the console
#
# Declaration of variables

files=("dir1.txt" "dir2.txt" "dir3.txt" "dir4.txt")

# Declaration of functions

filePath="fakefile.txt" 

if [ -e "$filePath" ]; then
    echo "File exists."
else
    echo "File does not exist. Creating new file."
    touch  "filePath"
    echo  "File created"
fi

number=1
while [ "$number" -le 2 ]; do
    echo "$number"
    ((number++))
done

# Main



# End