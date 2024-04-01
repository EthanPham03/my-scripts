#!/usr/bin/python3


import getpass
user = getpass.getuser
print(user)


import socket
ip_address = socket.gethostbyname
print(ip_address)


import platform
system_info = platform.uname()
print(system_info.system)
print(system_info.node)
print(system_info.release)
print(system_info.version)
print(system_info.machine)
print(system_info.processor)