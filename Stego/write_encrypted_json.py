# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 09:05:33 2022

@author: HoangMinh
"""

import nacl.secret
import nacl.utils
import json

def write_encrypted_json(obj, pin, file):
    obj = json.dumps(obj).encode("UTF-8")
    box = nacl.secret.SecretBox(pin)
    encrypted = box.encrypt(obj)
    ctext = encrypted.ciphertext
    nonce = encrypted.nonce
    with open(file,"wb") as f:
        f.write(ctext + nonce)