#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:32:17 2023

@author: NullCipherr
"""

# Transposition Encryption
def encrypt(message, key):
    # Initialize an empty list to store the encrypted message columns
    encrypted_message = [''] * key
    
    # Iterate through each column in the transposition grid
    for column in range(key):
        index = column
        # Traverse the message, adding characters to the current column
        while index < len(message):
            encrypted_message[column] += message[index]
            index += key
            
    # Concatenate the columns to form the encrypted message
    return ''.join(encrypted_message)

# Original message
message = "Encrypted message"

# Key for transposition (1 = Default message)
key = 10

# Encrypt the message using transposition cipher
encrypted_message = encrypt(message, key)

# Display the encrypted message
print("Encrypted message ->", encrypted_message)

