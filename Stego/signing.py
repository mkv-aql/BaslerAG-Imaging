# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 00:04:00 2022

@author: HoangMinh
"""
from nacl.signing import SigningKey, VerifyKey

#First we need to sign the image, pretend we can change it into byte type 
#object
def sign_and_verify(message):
    
    if type(message) != bytes:
        print("input must be of type byte")
        return None
    
    signing_key = SigningKey.generate()

    signed = signing_key.sign(message)

    signature = signed.signature
    
    try:
        #Checing everything is in place
        signing_key = SigningKey(signing_key._seed)
        verify_key = signing_key.verify_key.encode()
        verifier = VerifyKey(verify_key)
        verifier.verify(message, signature)
    except Exception as e:
        print(e)
        return (None, None, None)
    
    return signature, verify_key, signing_key._seed


if __name__ == "__main__":
    message = b'My name is Minh, I did this alone'
    signature, verify_key, seed = sign_and_verify(message)
    
    

