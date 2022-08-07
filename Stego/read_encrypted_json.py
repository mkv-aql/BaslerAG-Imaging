# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 09:44:02 2022

@author: HoangMinh
"""
import json 
import nacl.secret

def read_encrypted_json(filename, pin):
    with open(filename,'rb') as f:
        x = f.read()
    box = nacl.secret.SecretBox(pin)
    nonce = x[-24:]
    ctext = x[:(len(x)-24)]
    x = box.decrypt(ctext,nonce)
    x = json.loads(x)
    return x