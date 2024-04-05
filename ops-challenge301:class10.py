#!/usr/bin/env python3


# Declaration of variables


# Declaration of functions
touch('301lab10.txt')
with open('301lab10.txt') as file:
    file.write('A\n')
    file.write('B\n')
    file.write('C\n')

cat('301lab10.txt')

with open('301lab10.txt', 'r') as file:
    first_line = file.readline()
    print(first_line)
# Main


# End