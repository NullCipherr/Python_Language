#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:03:41 2023

@author: NullCipherr
"""

# Simple Substitution Encryption
def encrypt(alphabet, message, key):
    encrypted_message = ""
    
    for letter in message:
        # Consider lowercase, ignore spaces, and characters not present in the alphabet
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower())
            encrypted_letter = key[index]
            
            # Maintain the case (uppercase/lowercase) of the original letter
            if letter.isupper():
                encrypted_message += encrypted_letter.upper()
            else:
                encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    
    return encrypted_message


# Alphabet
alphabet = "abcdefghijklmnopqrstuvxwyz"

# Key
key = "zywxvutsrqponmlkjihgfedcba"

# Message to be encrypted
message = "Message to be encrypted"

# Encrypted message
encrypted_message = encrypt(alphabet, message, key)

print("Encrypted Message ->", encrypted_message)
