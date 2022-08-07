# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:41:43 2022

@author: HoangMinh
"""
from nacl.hash import sha256
import os
from StegoKeyGen import Key_Generate_for_Stego
from write_encrypted_json import write_encrypted_json
#from nacl.pwhash.argon2id import kdf #it takes too long

def deployer(pin_true, pin_fake):
    hash_pin_t = sha256(pin_true)[:15]
    hash_pin_f = sha256(pin_fake)[:15]
    hash_decoy = sha256(os.urandom(15))[:15]
    
    filename_f = str(hash_pin_f) + '.json'
    filename_t = str(hash_pin_t) + '.json'
    decoy_file = str(hash_decoy) + '.json'
    
    message_t = "I am safe00"
    message_f = "I am unsafe"
    message_decoy = "I am safe00"
    
    
    key_t = Key_Generate_for_Stego(120000,len(message_t)*8)
    key_f = Key_Generate_for_Stego(120000,len(message_f)*8)
    key_decoy = Key_Generate_for_Stego(120000,len(message_decoy)*8)
    
    contain_t = {'replace': decoy_file, 'key': key_t, 'message': message_t}
    contain_f = {'replace': filename_t, 'key': key_f, 'message': message_f}
    contain_decoy = {'replace': decoy_file, 'key': key_decoy, 'message': message_t}
    
    #Now put everything onto an encrypted file
    
    write_encrypted_json(contain_t, pin_true, filename_t)
    write_encrypted_json(contain_f, pin_fake, filename_f)
    write_encrypted_json(contain_decoy, pin_true, decoy_file)
    
    return filename_t, filename_f, decoy_file

if __name__=="__main__":
    pin_true = b'3\x9ap\x05],3YHn%\x83i|\xce\xb8\xefG\xcd\x06\xf39\x8d\x89\x9d\xf6\xedL\x15LS\xe2'
    pin_fake = b'#\x1a\xbc4\xa7;\'at"E7?\xfd\x7fo\xab5\n\x07|\xf0\x10:\xf0Pd<\xfd\xff\x18N'
    names = deployer(pin_true, pin_fake)
    