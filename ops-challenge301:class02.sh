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
echo "Current Date: $day.$month.$year"
echo "Current Time: $hour:$minute:$second"


# Main


# End