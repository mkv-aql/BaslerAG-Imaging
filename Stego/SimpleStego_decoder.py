# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 19:41:21 2022

@author: HoangMinh
"""

from matplotlib.pyplot import imread,imshow
import random
from PIL import Image
from StegoKeyGen import *
from change_character_name import change_charater_at_index
import numpy as np
from change_character_name import change_charater_at_index
import json 
import nacl.secret
import nacl.utils
from binary_to_bytes import *

def decoder(image, key, changes = None):
    check_decoder(key, changes)
    layer1 = image[:,:,0]
    x_dim, y_dim, layer_num = image.shape
    
    product = x_dim*y_dim
    carrier = layer1.reshape(product)
    
    total_bin = ''
    for i in range(len(key)):
        index = key[i]
        bin_code = format(carrier[index], "08b")
        total_bin += bin_code[-1]
        if changes[i] == 1:
            bit = str(1 - int(bin_code[-1]))
            carrier[index] = change_charater_at_index(bin_code, bit, -1)
    layer1 = carrier.reshape((x_dim, y_dim))
    image[:,:,0] = layer1
    return image, total_bin      
   
def check_decoder(key, changes):
    if changes != None:
        if len(key) != len(changes):
            raise ValueError("cannot undo changes since change list is not complete")
        if len(changes)%8 != 0:
            raise TypeError("changes must be devidable by 8")

def decoder_with_pin(im_file, key_file, pin_1):
    with open(key_file,'rb') as f:
        x = f.read()
    im = np.asarray(Image.open(im_file))
    box = nacl.secret.SecretBox(pin_1)
    nonce = x[-24:]
    ctext = x[:(len(x)-24)]
    x = box.decrypt(ctext,nonce)
    x = json.loads(x)
    _,message = decoder(im, x['key'], x['changes'])
    return binary_to_bytes(message)

if __name__=="__main__":
    pin_1 = b'Tr\xb4>(L\x1d\x8b\x06\x9cFR\x81\xa1\xd8\xe5\x0cNS\xd6\x95\x86\x84\xa6hdX\xe9-\xafi\x11'
    # with open('key_obj.json','rb') as f:
    #     x = f.read()
    # im = np.asarray(Image.open('encoded.png'))
    # box = nacl.secret.SecretBox(pin_1)
    # nonce = x[-24:]
    # ctext = x[:(len(x)-24)]
    # x = box.decrypt(ctext,nonce)
    # x = json.loads(x)
    # _,message = decoder(im, x['key'], x['changes'])
    
    assert decoder_with_pin("encoded.png",'key_obj.json', pin_1) == b"7"