from SplitCubeClass import parse
from hashTest import hash_
import numpy as np
import timeit
import copy

VALS_LEFT = ['0125637402301253', '0163572400342533', '0273415600331154',
             '0376125400031251', '0413265705501154', '0473651225002533',
             '0567123405302554', '1072463500501553', '2037465100004234',
             '2475360100504253', '2576130400301234', '2605347100331154',
             '2641357000332514', '3245706100301511', '3457160200002531',
             '3567012442542154', '4037256100004213', '4037562100504134',
             '4132560725041534', '4153072600301511', '4210537640541134',
             '4375016200031233', '4637512045531114', '4750263100004114',
             '5326701402331151', '6240753100331513', '6547123005542551',
             '6754231000001253', '7120534605041514', '7634210540041133']

vals_found = []
for val in VALS_LEFT:
    arr = [[int(val[0]), int(val[8])],
           [int(val[1]), int(val[9])],
           [int(val[2]), int(val[10])],
           [int(val[3]), int(val[11])],
           [int(val[4]), int(val[12])],
           [int(val[5]), int(val[13])],
           [int(val[6]), int(val[14])],
           [int(val[7]), int(val[15])], # Last value doesn't matter so set it to something that won't be affected
           [0, 0]] # These vals are present so that parse() works properly. They aren't useful for any part of this program
    vals_found.append(arr)


move_len_arr = np.load('corners.npy')

MOVES = np.array([['w', 0], ['W', 1],
                  ['y', 2], ['Y', 3],
                  ['r' ,4], ['R', 5],
                  ['o', 6], ['O', 7],
                  ['b', 8], ['B', 9],
                  ['g', 10], ['G', 11],
                  ['WW', 12], ['YY', 13],
                  ['RR', 14], ['OO', 15],
                  ['BB', 16], ['GG', 17],])

def arr_to_str(arr):
    first_half = ''
    second_half = ''
    for x in range(8):
        first_half += str(arr[x][0])
        second_half += str(arr[x][1])
    
    return first_half + second_half
  
    
def search(root):
    
    viable_distance = []
    for move in MOVES:
        new = copy.deepcopy(root)
        parse(new, move[0])
        if move_len_arr[hash_(arr_to_str(new))] == 12:
            viable_distance.append(search(arr_to_str(new))+1)
        else:
            viable_distance.append(move_len_arr[hash_(arr_to_str(new))]+1)
    return min(viable_distance)

for val in vals_found:
    # Run an custom search on each of the values to find the shortest path to the goal
    # state, using the successfully computed states
    print(val)
    move_len_arr[hash_(arr_to_str(val))] = search(val)
    np.save('corners.npy', move_len_arr)
