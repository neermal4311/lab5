#!/usr/bin/env python3
# Author ID: ngautam11

def add(number1, number2):
    try:
        number1 = int(number1)
        number2 = int(number2)
        return number1 + number2
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works
    print(add('10', 5))                      # now should work
    print(add('abc', 5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
