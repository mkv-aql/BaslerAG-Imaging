#Transform an image to bytes object

from matplotlib.pyplot import imread,imshow, savefig
import random
from StegoKeyGen import *
from change_character_name import change_charater_at_index
import numpy as np
import json
from PIL import  Image



def encoder(image, message, key):
    layer1 = image[:,:,0]
    x_dim, y_dim, layer_num = image.shape
    
    product = x_dim*y_dim
    
    changes = ()
    # 0 means unchange, 1 means change
    encoder_check(x_dim, y_dim,layer_num, message, key,)
    
    carrier = layer1.reshape(product)
    for enum1,x in enumerate(message):
        for enum2,bit in enumerate(format(x,"08b")):
            index_on_carrier = key[enum1*8 + enum2]
            pixel_value_in_bin = format(carrier[index_on_carrier], '08b')
            if pixel_value_in_bin[-1] != bit:
                changes += (1,)
                #pixel_value_in_bin[-1] = bit
                pixel_value_in_bin = change_charater_at_index(pixel_value_in_bin, 
                                                              bit, -1)
                carrier[index_on_carrier] = int(pixel_value_in_bin,2)
            else: 
                changes += (0,)
    image_with_message = carrier.reshape((x_dim, y_dim))
    image[:,:,0] = image_with_message
    #key_object = {'key': key, 'changes': changes}
    #json_dumps_with_pin(key_object)
    im = Image.fromarray(image)
    im.save('encoded.png')
    return changes

def encoder_check(x_dim, y_dim,layer_num, message, key):
    #kex_length must be at least 8 times message length
    if len(key) < 8*len(message):
        raise ValueError('key is not length enough. Key is an array of integer with length at least 8 time the message.')
    if type(message) != bytes:
        raise TypeError('message must be of type bytes')
    if 8*len(message) > x_dim*y_dim:
        raise ValueError("Image doesn't have sufficient resolution for this message. Please reduce message length or choose another image.")
        
def encoder_with_pin(image, message, key, pin_1):
    changes = encoder(image, message, key)
    key_obj ={"key": key, 'changes': changes}
    key_obj = json.dumps(key_obj).encode("UTF-8")
    box = nacl.secret.SecretBox(pin_1)
    encrypted = box.encrypt(key_obj)
    ctext = encrypted.ciphertext
    nonce = encrypted.nonce
    with open("key_obj.json","wb") as f:
        f.write(ctext + nonce)
        #nonce always has length 24
    
    

if __name__=='__main__':
    image = imread('dog.jpg')

    #message = b"I did this alone"
    
    message = b'7'
    key = Key_Generate_for_Stego(120000,len(message)*8)
   
   # key = [1,2,3,4,5,6,7,8]
    #image, changes = encoder(image, message, key)
    pin_1 = b'Tr\xb4>(L\x1d\x8b\x06\x9cFR\x81\xa1\xd8\xe5\x0cNS\xd6\x95\x86\x84\xa6hdX\xe9-\xafi\x11'
    
    encoder_with_pin(image, message, key, pin_1)
    
    
    
            