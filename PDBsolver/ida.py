from . import common
from . import hasher
hash_ = hasher.hash_
import copy
import numpy as np

# Load PDBs
def load():
    global CORNERS_PDB, EDGES1_PDB, EDGES2_PDB
    try:
        CORNERS_PDB = np.load('PDBsolver/DBs/corners.npy')
        EDGES1_PDB  = np.load('PDBsolver/DBs/edges1.npy')
        EDGES2_PDB = np.load('PDBsolver/DBs/edges2.npy')
    except FileNotFoundError:
        print('PDBs not present, generating now. This will take some time.')
        import generatePDBs
        generatePDBS.IDDFS(common.CUBE_INIT, input('PDB generation depth: '))
        CORNERS_PDB = np.load('PDBsolver/DBs/corners.npy')
        EDGES1_PDB  = np.load('PDBsolver/DBs/edges1.npy')
        EDGES2_PDB = np.load('PDBsolver/DBs/edges2.npy') 

def unload():
    global CORNERS_PDB, EDGES1_PDB, EDGES2_PDB
    del CORNERS_PDB, EDGES1_PDB, EDGES2_PDB

def heur(state):
    '''Estimate the distance to the goal state'''
    h = hash_(state)
    # Only admissible heuristic is the maximum of the PDBs
    return max(CORNERS_PDB[h[0]], EDGES1_PDB[h[1]], EDGES2_PDB[h[2]])

def successors(node):
    '''Generate the child nodes of a given state'''
    MOVES = ['W','w',
             'Y','y',
             'R','r',
             'O','o',
             'B','b',
             'G','g']
    li = []
    for move in MOVES:
        n = copy.deepcopy(node) # Create a copy of the parent node
        common.parse(n, move) # Execute a move on it
        li.append((heur(n), n)) # add it to the list
    for i in sorted(li):
        yield i

def Astar(root):
    load()
    '''Execute an IDA* search to find the ideal soloution'''
    root[2] = '' # Reset the parent node's move list
    threshold = heur(root) # Calculate the current distance to the goal
    if threshold == 20:
        unload()
        return -1 # Early out if the cube is at a depth greater than the PDBs are generated to
    while 1:
        temp = search(root, 0, threshold, heur(root))
        if type(temp) == type(root): # If the goal node has been found
            unload()
            return temp[2] # Return the move list
        if temp == 20: # If the root node isn't solveable
            unload()
            return -1
        threshold = temp # If the goal hasn't been found, increase the threshold
                         # to the minimum value required to go deeper

def search(node, g, threshold, h): # Recursive function
    # g is distance from root to current
    f = g+h # Calculate the total distance from root to goal
    if f > threshold: # If the distance is higher than current max allowed
        return f # Return that distance to increase the threshold
    if common.isSolved(node): # If the current node is the goal
        return node # Return the goal node so the path can be returned
    minim = float('inf') 
    for he, child in successors(node): # Iterate over each child node
        temp = search(child, g+1, threshold, he) # Check child nodes.
                        # g+1 as another move has been performed
        if type(temp) == type(node): # If the goal node has been found
            return temp # Send it further up the chain
        if temp < minim: # Find the minimum value required to explore new nodes
            minim=temp
    return minim # if the goal hasn't been found, expand the search


if __name__ == '__main__':
    arr = copy.deepcopy(common.CUBE_INIT) # Create the cube array
    common.parse(arr, 'ywrY') # parse some moves to try search
    #print(heur(arr))
    a = Astar(arr) # Run the search
    print(a) # Output the results
