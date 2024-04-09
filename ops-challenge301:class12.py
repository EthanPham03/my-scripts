#!/usr/bin/env python3


# Declaration of variables
import requests
import get 

http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']

# Declaration of function
response = request.get('https://api.github.com')

print(response.header)

print("Select an HTTP Method:")
selection = input(http_methods)

print("Please confirm before proceeding")


# Main


# End