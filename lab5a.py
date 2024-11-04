#!/usr/bin/env python3
#Nirmal Gautam - ngautam11 - OPS445ZAA

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))


