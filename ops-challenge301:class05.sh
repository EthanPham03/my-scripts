#!/bin/bash

# Script Name:                  ops301-challenge03-Clearing-Logs
# Author:                       Ethan Pham
# Date of latest revision:      03/29/2024
# Purpose:                      Create a script that clears log files for the user. 

# Declaration of variables

# Declaration of functions
mkdir backup_directory
BACKUP_DIR="backup_directory"
timestamp=$(date +%Y-%m-%d_%H-%M-%S)

log_dir="log_files"

tar -czvf "$/var/log/backups/syslog-20240329054600.zip" /var/log/syslog 
tar -czvf "$/var/log/backups/wtmp-20240329054600.zip" /var/log/wtmp

echo "Log files have been compressed"

truncate -s 0 /var/log/syslog /var/log/wtmp

backup_file_size=$(du -h "$/var/log/backup/syslog-20240329054600.zip" | awk '{print $1}')
backup_file_size=$(du -h "$/var/log/backup/wtmp-20240329054600.zip" | awk '{print $1}')

# Main


# End