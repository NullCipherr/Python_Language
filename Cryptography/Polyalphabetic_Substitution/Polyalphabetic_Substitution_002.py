#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:06:16 2023

@author: NullCipherr
"""

# Polyalphabetic Substitution Encryption
def encrypt(message, key) :
    encryptedMessage = ""
    key_length = len(key)
    
    for i in range(len(message)) :
        char = message[i]
        
        # Process only alphabetic characters
        if char.isalpha() : 
            # Repeating key, case-insensitive
            key_char = key[i % key_length].lower()
            
            # Convert key character to a shift value
            shift = ord(key_char) - ord('a')
            encrypted_char = encrypt_char(char, shift)
            encryptedMessage += encrypted_char
        else:
            # Preserve non-alphabetic characters
            encryptedMessage += char
    
    return encryptedMessage

def encrypt_char(char, shift):
    # Encrypt a single alphabetic character
    if char.isupper() :
        return chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
    elif char.islower() :
        return chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
    else :
        return char

# Original message
message = "Encrypt this message"

# Key for polyalphabetic substitution
key = "PRIVATE"

# Encrypt the message using polyalphabetic substitution cipher
encryptedMessage = encrypt(message, key)

# Display the encrypted message
print("Encrypted message ->", encryptedMessage)