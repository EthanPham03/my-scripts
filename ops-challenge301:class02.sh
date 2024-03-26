#!/bin/bash

# Script Name:                  ops301-challenge02-Append;-date-and-time
# Author:                       Ethan Pham
# Date of latest revision:      03/26/2024
# Purpose:                      Manipulate a variable in bash to apply today's date to a log file
#
# Declaration of variables
year=`date +%Y`
month=`date +%m`
day=`date +%d`

hour=`date +%H`
minute=`date +%M`
second=`date +%S`


# Declaration of functions
if [ -f "/var/log/syslog" ]; then
    # Copy /var/log/syslog to the current working directory
    cp /var/log/syslog .
    echo "Copied /var/log/syslog to the current working directory."
else
    echo "Error: /var/log/syslog not found."
fi


echo "Current Date: $day.$month.$year" >> testfile.txt
echo "Current Time: $hour:$minute:$second" >> testfile.txt

echo "Original file before append:"
cat testfile.txt


# Main


# End