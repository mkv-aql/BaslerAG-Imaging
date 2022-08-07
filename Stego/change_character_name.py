# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 01:55:34 2022

@author: HoangMinh
"""

def change_charater_at_index(original, character, index):
    if type(original) != str or type(character) != str:
        raise TypeError("We need a string for both input")
    if type(index) != int:
        raise TypeError("We need an integer for index")
    original = list(original)
    original[index] = character
    k =''
    for x in original:
        k += x
    return k