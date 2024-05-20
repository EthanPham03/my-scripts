#!/bin/usr/python3

# Script Name:                      401 ops challenge 16
# Author:                           Ethan Pham
# Date of latest revision:          May 20, 2024
# Purpose:                          Create a Wordlist Attack Tool

import time

def offensive_mode(file_path, delay):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
        for word in words:
            word = word.strip()
            print(word)
            time.sleep(1)
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
            offensive_mode(file_path)
        elif mode == '2':
            search_string = input("Enter string to search: ")
            file_path = input("Enter word list file path: ")
            defensive_mode(file_path, search_string)
        
        break

if __name__ == "__main__":
    main()