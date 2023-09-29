#!/usr/bin/env python 
import random

flag = 'flag-for_God_and_Liberty'

def print_key(key, number):
    print(f"char key{number}[24] = " + '{', end='')
    for i in range(len(key) - 1):
        print(f'{hex(key[i])}, ', end='')
    print(f'{hex(key[-1])}' + '};')

def compute_keys(flag):
    key1 = []
    key2 = []
    key3 = []
    key4 = []

    for i in range(len(flag)):
        key1.append(random.randint(0, 255))
        key2.append(random.randint(0, 255))
        key3.append(random.randint(0, 255))
        key4.append(ord(flag[i]) ^ key1[i] ^ key2[i] ^ key3[i])

    # print_key(key1, 1)
    # print_key(key2, 2)
    # print_key(key3, 3)
    # print_key(key4, 4)
    return [*key1, *key2, *key3, *key4]

def obfuscate_value(intended_value, number_of_values_present, values):
    obfuscated_string = ''
    new_values_indexes = [] # The indexes of the values that, together, compose the obfuscated value
    total = 0

    for _ in range(random.randint(max(1, number_of_values_present - 10), number_of_values_present)):
        random_valid_index = random.randint(0, number_of_values_present - 1)
        total += values[random_valid_index]
        new_values_indexes.append(random_valid_index)

    for index in new_values_indexes[:-1]:
        obfuscated_string += f"keys[{index}] + "

    obfuscated_string += f"keys[{new_values_indexes[-1]}] "

    if total > intended_value:
        obfuscated_string += f"- {total - intended_value};"
    else:
        obfuscated_string += f"+ {intended_value - total};"

    return obfuscated_string

def obfuscate_keys(keys):
    obfuscated_function = f'\tkeys[0] = {hex(keys[0])};\n'
    for i in range(1, len(keys)):
        obfuscated_function += f'\tkeys[{i}] = ' + obfuscate_value(keys[i], i, keys) + '\n'
    print(obfuscated_function)

keys = compute_keys(flag) # This computes the four xor keys that, when xored, compose the flag
obfuscate_keys(keys)      # This obfuscates the individual values that compose the keys and prints
                          # the corresponding C function
