# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:17:28 2022

@author: HoangMinh
"""
from PIL import Image
import numpy as np
from Cryptodome.Cipher import AES
from key_generator.key_generator import generate
import matplotlib.pyplot as plt

def Splitting_into_layer(Image_Adress):
    im = Image.open(Image_Adress, 'r')
    imarray = np.array(im)
    x,y,z = imarray.shape

    a = [imarray[:,:,j] for j in range(z)]
    a = tuple(a)
    return a 
# a is a tuple of the 3 Layers

def encrypt_image(Image_Adress):
        layers = Splitting_into_layer(Image_Adress)
        key = generate(num_of_atom =1, min_atom_len = 16, max_atom_len = 16) 
        key = key.get_key()
        key = key.encode('utf-8')
        encrypter = AES.new(key, AES.MODE_CBC, IV = b'0000000000000000')
        ciphers = []
        x,y = layers[0].shape
        ciphers = np.zeros((x,y,3))
        i=0
        for layer in layers:
            vector_of_layer = layer.reshape((1,x*y))
            bytes_data = vector_of_layer.tobytes()
            ciphertext = encrypter.encrypt(bytes_data)
            cipher_image = np.frombuffer(ciphertext, dtype = 'uint8').reshape((x,y))
            ciphers[:,:,i] = cipher_image
            i+=1
        cipher_image = Image.fromarray(np.uint8(ciphers))
        cipher_image.save("cipher_image.png","PNG")
        return key, b'0000000000000000', "cipher_image.png"
    #Cipher contains the encryption of each layer

def decrypt_image(key, IV,Image_Adress):
    layers = Splitting_into_layer(Image_Adress)
    decrypter = AES.new(key, AES.MODE_CBC, IV)
    x,y = layers[0].shape
    plains = np.zeros((x,y,3))
    i=0
    for layer in layers:
        vector_of_layer = layer.reshape((1,x*y))
        bytes_data = vector_of_layer.tobytes()
        plaintext = decrypter.decrypt(bytes_data)
        plain_image = np.frombuffer(plaintext, dtype = 'uint8').reshape((x,y))
        plains[:,:,i] = plain_image
        i+=1
    plain_image = Image.fromarray(np.uint8(plains))
    plain_image.save("plain_image.png","PNG")

if __name__ == '__main__':
   key, IV, Image_Adress = encrypt_image('dog.12499.jpg')
   decrypt_image(key, IV, Image_Adress)
   