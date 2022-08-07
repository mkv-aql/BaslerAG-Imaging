# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:33:39 2022

@author: HoangMinh
"""

def binary_to_bytes(bin_str):
    check_binary_to_bytes(bin_str)
    byte_obj = []
    for x in range(len(bin_str)//8):
        byte = ''
        for j in range(8):
            byte += bin_str[x*8+j]
        byte_obj += [int(byte,2),]
    
    return bytes(byte_obj)
    
def check_binary_to_bytes(bin_str):
    if len(bin_str) % 8 != 0:
        raise ValueError("binary stirng must has length multiple of 8")


if __name__ == "__main__":
    bin_str = ""
    in_message = "I did this alone".encode("UTF-8")
    for x in in_message:
        bin_str += format(x, "08b")
    out_message = binary_to_bytes(bin_str)
    print(in_message == out_message)
    