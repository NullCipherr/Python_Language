#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:53:55 2023

@author: NullCipherr
"""

def encrypt(message, key):
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""

    # Iterate through each character in the message
    for i in range(len(message)):
        letter = message[i]

        # Check if the character is an alphabetic letter
        if letter.isalpha():
            # Check if the letter is lowercase
            if letter.islower():
                # Encrypt the lowercase letter and add it to the encrypted message
                encrypted_message += chr((ord(letter) + key - 97) % 26 + 97)
            else:
                # Encrypt the uppercase letter and add it to the encrypted message
                encrypted_message += chr((ord(letter) + key - 65) % 26 + 65)
        else:
            # Preserve non-alphabetic characters in the encrypted message
            encrypted_message += letter

    # Return the final encrypted message
    return encrypted_message

# Original message
message = "Encrypt this message"

# Key for encryption (in this case, set to 5 for a shift of 5 positions)
key = 5

# Encrypt the message using the specified key
encrypted_message = encrypt(message, key)

# Display the encrypted message
print("Encrypted message ->", encrypted_message)
