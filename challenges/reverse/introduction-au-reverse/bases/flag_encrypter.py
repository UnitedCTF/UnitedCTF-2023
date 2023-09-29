#!/usr/bin/env python
from random import random

flag = 'flag-engineering'
key = 'drunken-sailor'
encrypted_flag = [''] * 16 * 4

def random_number(max):
    return int(random() * max)

for i in range(len(flag)):
    print(f'Current char: {flag[i]}')
    current_number = ord(flag[i])
    current_key = ord(key[i % len(key)])

    inputed_number = random_number(current_number)
    current_number -= inputed_number
    encrypted_flag[i + 0 * len(flag)] = inputed_number ^ current_key

    inputed_number = random_number(current_number)
    current_number -= inputed_number
    encrypted_flag[i + 1 * len(flag)] = inputed_number ^ current_key

    inputed_number = random_number(current_number)
    current_number -= inputed_number
    encrypted_flag[i + 2 * len(flag)] = inputed_number ^ current_key

    encrypted_flag[i + 3 * len(flag)] = current_number ^ current_key

print(f'Encrypted flag = {encrypted_flag}')