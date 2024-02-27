#!/bin/bash

# Script Name:                  ops201-challenge07-system-information
# Author:                       Ethan Pham
# Date of latest revision:      02/27/2024
# Purpose:                      Createa script that uses lshw to display system information to the screen about the following components: Name of the computer; CPU; RAM; Diplay adapter; Network adapter.  

# Declaration of variables


# Declaration of functions
echo "Name of computer"
sudo lshw -class system | grep -E 'description' | awk '{print $2}'
echo "CPU"
sudo lshw -class cpu | grep -E 'product:|vendor:|physical id:|bus info:|width:' | awk '{print $2}'
echo "RAM"
sudo lshw -class memory | grep -E 'description:|physical id:|size:' | awk '{print $2}'
echo "Display adapter"
sudo lshw -class display | grep -E 'description:|product:|vendor:|physical id:|bus info:|width:|clock:|capabilities:|configuration:|resources:' | awk '{print $2}'
echo "Network adapter"
sudo lshw -class network | grep -E 'description:|product:|vendor:|physical id:|bus info:|logical name:|version:|serial:|size:|capacity:|width:|clock:|capabilities:|configuration:|resources:' | awk '{print $2}'

# Main



# End