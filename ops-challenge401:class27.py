#!/bin/usr/python3

# Script Name:                      401 ops challenge 27
# Author:                           Ethan Pham
# Date of latest revision:          Jun 4, 2024
# Purpose:                          Add log rotation feature based on size

import os
import logging
from logging.handlers import RotatingFileHandler
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

log_handler = RotatingFileHandler('class26.log', maxBytes=5*1024*1024, backupCount=5, encoding='utf-8')
log_handler.setLevel(logging.DEBUG)

logger= logging.getLogger(__name__)
logger.addHandler(log_handler)

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

def main():
    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Perform logging")

    mode = input("Enter mode (1/2/3/4/5): ")

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
        logger.info("Logging selected")
        try:
            logger.debug("Debug log")
            logger.error("Error log")
            print("logging placed in class26.log")
        except Exception as e:
            logger.exception("Exception occured")

    else:
        logger.error("Invalid mode selected.")
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()