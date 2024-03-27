#!/bin/bash

# Script Name:                  ops301-challenge03-File-Permissions
# Author:                       Ethan Pham
# Date of latest revision:      03/27/2024
# Purpose:                      Create a bash script that alters file permissions of everything in a directory
#
# Declaration of variables

# Declaration of functions
echo "Enter directory path for permissions"
read directory_path 

echo "Enter a permissions number (e.g. 777)"
read permissions

chmod -R "$permissions" .

echo "Permissions of files in '$directory_path' have been changed to '$permissions'." 

echo "Directory Contents and New Permissions Settings"
ls -1 | awk '{print $1,$NF}'

# Main


# End