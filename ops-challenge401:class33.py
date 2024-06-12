#!/bin/usr/python3

# Script Name:                      401 ops challenge 33
# Author:                           Ethan Pham
# Date of latest revision:          Jun 12, 2024
# Purpose:                          Add ability to connect to Virustotal and compare hashes

import os
import hashlib
import datetime

def generate_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except Exception as e:
        return f"Error generating MD5: {e}"
    return hash_md5.hexdigest()

def check_virus_total(md5_hash, api_key):
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    params = {'apikey': apikey, 'resource': md5_hash}
    try:
        response = requests.get(url, params=params)
        response_json = response_json()
        if response_json['response_code'] == 1:
            positive = response_json['positives']
            total = response_json['total']
            return positive, total
        else:
            return None, None
    except Exception as e:
        return f"Error connecting to VirusTotal: {e}", None

def search_files(search_directory):
    files_searched = 0
    hits_found = 0

    for root, dirs, files in os.walk(search_directory):
        for file in files:
            files_searched += 1
            full_path = os.path.join(root, file)
            md5_hash = generate_md5(full_path)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_size = os.path.getsize(full_path)

            print(f"Timestamp: {timestamp}")
            print(f"File: {file}")
            print(f"File Path: {full_path}")
            print(f"File Size: {file_size} bytes")
            print(f"MD5 Hash: {md5_hash}")

            positives, total = check_virus_total(md5_hash, api_key)
            if positives is not None:
                print(f"VirusTotal Positives: {positives}")
                print(f"VirusTotal Total: {total}")
                if positives > 0:
                    hits_found += 1
            else:
                print("File not found in VirusTotal database")

    print(f"Files searched: {files_searched}")
    print(f"Files with positives detected: {hits_found}")

if __name__ == "__main__":
    directory_to_search = input("Enter directory to search in: ")
    api_key = "API_KEY_VIRUSTOTAL"

    if os.path.isdir(directory_to_search):
        search_files(file_name_to_search, directory_to_search)
    else:
        print("Directory does not exist.")