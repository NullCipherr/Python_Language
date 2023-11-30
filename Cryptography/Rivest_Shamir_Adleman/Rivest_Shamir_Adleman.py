#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:13:36 2023

@author: NullCipherr
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# RSA Encryptation
try:
    # Key Generation
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()

    # Encrypt Message
    message = b"This is a secret message"
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher_rsa.encrypt(message)
    print("Encrypted Message:", encrypted_message)

    # Decrypt Message
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message.decode())

except Exception as e:
    print(f"An error occurred: {e}")
