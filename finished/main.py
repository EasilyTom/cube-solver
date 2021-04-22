from SplitCubeClass import parse
from hashTest import hash_
import copy
import numpy as np
import time
from collections import deque
import multiprocessing as mp


move_len_arr = np.full(88179840, 12, dtype=np.int8)
i = 0

def arr_to_str(arr):
    first_half = ''
    second_half = ''
    for x in range(8):
        first_half += str(arr[x][0])
        second_half += str(arr[x][1])
    
    return first_half + second_half
                
def make_graph(state):
    
    MOVES = ['w', 'W',
             'y', 'Y',
             'r', 'R',
             'o', 'O',
             'b', 'B',
             'g', 'G']
    global i
    global queue
    
    while len(queue):
        node = queue.popleft()
        _str = arr_to_str(node)
        hashed_val = hash_(_str)
        if node[8] < move_len_arr[hashed_val]:
            i += 1
            move_len_arr[hashed_val] = node[8]
            node[8] += 1
            for move in MOVES:
                new = copy.deepcopy(node)
                parse(new, move)
                queue.append(new)
            if i%10000 == 0:
                print(i)

    
if __name__ == '__main__':
    start = time.time()
    queue = deque()
    arr = [[0, 0], [1, 0], [2, 0], [3, 0],[4, 1], [5, 1], [6, 1], [7, 1], 0]
    queue.append(arr)

    #procs = []
    procs = mp.Process(target=make_graph)
    procs.start()
    procs.join()
    
    #np.save('corners.npy', move_len_arr)
    #print('Time taken: ', str(start - time.time()))
