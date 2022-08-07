# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:46:26 2022

@author: HoangMinh
"""

from signing import sign_and_verify
from PIL import Image
import numpy as np
from SimpleStego import encoder
from StegoKeyGen import *
import time


start = time.time()
im = Image.open("dog.jpg")
im = np.asarray(im)
layer_0 = im[:,:,0].reshape(120000)
im_bytes = bytes(layer_0)
signature, verify_key, private_key = sign_and_verify(im_bytes)
x_dim, y_dim, z_dim = im.shape
key = Key_Generate_for_Stego(x_dim*y_dim,len(signature)*8)
_,changes = encoder(im, signature, key)

stop = time.time()



