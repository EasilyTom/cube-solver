from SplitCubeClass import parse
from hashTest import hash_
import numpy as np
import timeit
import copy

move_len_arr = np.full(88179840, 12, dtype=np.int8)
vals_checked = 0
MOVES = np.array([['w', 0], ['W', 1],
                  ['y', 2], ['Y', 3],
                  ['r' ,4], ['R', 5],
                  ['o', 6], ['O', 7],
                  ['b', 8], ['B', 9],
                  ['g', 10], ['G', 11],
                  ['WW', 12], ['YY', 13],
                  ['RR', 14], ['OO', 15],
                  ['BB', 16], ['GG', 17]])
    

def arr_to_str(arr):
    first_half = ''
    second_half = ''
    for x in range(8):
        first_half += str(arr[x][0])
        second_half += str(arr[x][1])
    
    return first_half + second_half

def update_len_arr(state):
    global vals_checked
    hashed = hash_(arr_to_str(state))
    if move_len_arr[hashed] > state[8][0]:
        move_len_arr[hashed] = state[8][0]
        vals_checked += 1
        if vals_checked % 10000 == 0:
            print(vals_checked)
        return True
    elif move_len_arr[hashed] == state[8][0]:
        return True
    else:
        return False
    
def DLS(root, max_depth):
    if not update_len_arr(root):
        return
    if max_depth <= 0:
        return
    
    for move in MOVES:
        newmove = int(move[1])
        if newmove != root[8][1] :
            new = copy.deepcopy(root)
            parse(new, move[0])
            new[8][1] = newmove
            DLS(new, max_depth - 1)
        
def IDDFS(root, max_depth):
    for i in range(max_depth):
        DLS(root, i)
        print('finished depth ', i)

if __name__ == '__main__':
    arr = [[0, 0], [1, 0], [2, 0], [3, 0],[4, 1], [5, 1], [6, 1], [7, 1], [0, 20]] # last sublist contains depth and last move
    IDDFS(arr, 12)
    
