#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables

### Read user input here into a variable

# Declaration of functions

### Declare a function here
def main():
    directory = 'dir1' 
    dir1 = input("Please enter file path") 

for (root, dirs, files) in os.walk("dir1"):
    file_path = os.path.join(directory, 'dir1.txt')
    file_content = read_file_content(file_path)
        print(root)
        print(files)

# Main

### Pass the variable into the function here

# End