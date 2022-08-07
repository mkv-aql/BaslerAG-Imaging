# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 00:55:31 2022

@author: HoangMinh
"""
import random

#create an array of length which contains indices of pixels, in which the message 
#is embedded in 
def Key_Generate_for_Stego(stop, length):
    if length > stop:
        raise "message length must be less than image size"
    values = [x for x in range(stop)]
    key = ()
    while len(key) < length:
        x = random.choice(values)
        if x != None:
            key = key + (x,)
            values[x] = None
    return key