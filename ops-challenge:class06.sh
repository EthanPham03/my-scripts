#!/bin/bash

# Script Name:                  ops201-challenge06-conditionals
# Author:                       Ethan Pham
# Date of latest revision:      02/26/2024
# Purpose:                      Create a scripe that detects if a file or directory exists, then creates it if it does not exist. 

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