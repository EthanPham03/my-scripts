#!/bin/usr/python3

# Script Name:                      401 ops challenge 37
# Author:                           Ethan Pham
# Date of latest revision:          Jun 18, 2024
# Purpose:                          Copy the demo script and complete the objectives. 

import requests

initial_url = 'http://www.dev2qa.com'

initial_response = requests.get(initial_url)
captured_cookies = initial_response.cookies

print("Captured Cookies:")
for cookie in captured_cookies:
    print(f"cookie domain = {cookie.domain}")
    print(f"cookie name = {cookie.name}")
    print(f"cookie value = {cookie.value}")
    print("*************************************")

cookies_dict = {}
for cookie in captured_cookies:
    cookies_dict[cookie.name] = cookie.value

subsequent_url = 'https://www.dev2qa.com'

response = requests.get(subsequent_url, cookies=cookies_dict)

print("Response Text:")
print(response.text)