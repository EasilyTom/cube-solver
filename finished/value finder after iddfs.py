import numpy as np
import hashForAfterIDDFS as hashTest

def arr_to_str(arr):
    first_half = ''
    second_half = ''
    for x in range(8):
        first_half += str(arr[x][0])
        second_half += str(arr[x][1])
    
    return first_half + second_half

arr12 = np.load('arr12.npy') # Load the list of hashes which haven't been found yet
CONSTANTS = [11022480, 1574640, 262440, 52488, 13122, 4374, 2187]
print('arr12 is ', arr12)
print('intialising values')
values = hashTest.make_test_list()
print('values initialised')
print('hashing values')
hashed = []
for x in values:
    hashed.append(hashTest.hash_(x))
print('values hashed')
print('finding values')
found_vals = []
for ind in arr12:
    valind = hashed.index(ind)
    found_vals.append(values[valind])
print('values found')
print(found_vals)
