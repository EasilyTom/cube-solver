import numpy as np
import bitarray

def get_ones(num):
    
        

def pre_populate():
    arr = []
    for i in range(0, 256):
        arr.append()

    
def right_shift(ba, count):
    return (bitarray.bitarray('0') * count) + ba[:-count]

def hash_(val):
    """Return the hashed value of a cube state

    val must be a string 8888888866666666"""
    
    bstring = bitarray.bitarray('00000000')
    lehmer = ''
    for char in val:
        bstring[char] = True
        temp_bstring = right_shift(bstring, 8-int(char))
        
        
    

        
if __name__ == '__main__':
    hash_('0123456700000000')
