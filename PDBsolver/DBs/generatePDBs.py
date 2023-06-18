from .. import common
from .. import hasher
import numpy as np
import copy

corners = np.full(88179840, 20, dtype=np.int8) # Create the array used as the PDB
#12P7 * 2**7 = 510935040

edges1 = np.full(510935040, 20, dtype=np.int8)
edges2 = np.full(510935040, 20, dtype=np.int8)
#12P7 * 2**7 = 510935040

checked_states = 0 # Number unique states that have been visited.
# Not guaranteed to be accurate but will be close.


def heur(state):
    '''Return true if we should explore this branch'''
    global checked_states
    hash_val = hasher.hash_(state) # Hash the state
    DEPTH = len(state[2])
    ret = False
    if DEPTH < corners[hash_val[0]]:
        corners[hash_val[0]] = DEPTH
        checked_states += 1
        if checked_states % 10000 == 0: print(checked_states)
        ret = True
    
    if DEPTH < edges1[hash_val[1]]:
        edges1[hash_val[1]] = DEPTH
        checked_states += 1
        if checked_states % 10000 == 0: print(checked_states)
        ret = True
    
    if DEPTH < edges2[hash_val[2]]:
        edges2[hash_val[2]] = DEPTH
        checked_states += 1
        if checked_states % 10000 == 0: print(checked_states)
        ret = True
    
    return (ret or
            DEPTH == corners[hash_val[0]] or
            DEPTH == edges1[hash_val[1]] or
            DEPTH == edges2[hash_val[2]])


def DLS(root, max_depth):

    if max_depth < 0:
        return

    if heur(root): # If this is the shortest path to this node
        MOVES = ['W','w',
                 'Y','y',
                 'R','r',
                 'O','o',
                 'B','b',
                 'G','g']

        for move in MOVES:
            n = copy.deepcopy(root) # Create a copy of the current node
            common.parse(n, move) # And execute a move on it
            DLS(n, max_depth-1) # Then recur from that node with depth decremented

def IDDFS(root, max_depth):
    for x in range(max_depth+1):
        DLS(root, x)
        print('Finished Depth ', x)
        
    global corners, edges1, edges2
    np.save('PDBsolver/DBs/corners', corners)
    np.save('PDBsolver/DBs/edges1', edges1)
    np.save('PDBsolver/DBs/edges2', edges2)










        
