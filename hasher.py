import multiprocessing as mp

def hash(cube):
    '''Given a CubeClass.Cube object, create the 3 hash values of it
        Returns the hashes as a touple (corners, first, second)'''
    return (_hash_corners(cube[0]),
            _hash_edges(cube[1], False),
            _hash_edges(cube[1], True))

def _hash_corners(val):
    """Return the hashed value of a cube state's corners"""
    # The final corner is determined by the first 7 so is irrelevant
    val = val[:-1]

    # First the orientation of each corner is dealt with
    second_half_2 = 0
    for i, x in enumerate(val):
        second_half_2 += x[1] * (3**(6-i))
    # Then the permutation
    bitset = [0, 1, 2, 3, 4, 5, 6, 7]
    def get_num(i):
        '''Find how far a corner is from where it should be'''
        num = bitset.index(i)
        del bitset[num]
        return num

    DIVISIONS = [11022480, 1574640, 262440, 52488, 13122, 4374, 2187]
    # The values in DIVISIONS are all decreasing factors of 88179840
    # Which is the total number of corner permutations

    for i, z in enumerate(val):
        index += get_num(z[0]) * DIVISIONS[i]

    return index

def _hash_edges(state, end):
    """Return the hashed value of a cube state's edges"""

    def reformat(state):
        '''Seperate the state into permutation and orientation'''
        fhalf = []
        shalf = ''
        for x in state:
            fhalf.append(x[0])
            shalf += str(x[1])
        return fhalf, int(shalf, 2)

    bitset = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    def get_num(i):
        '''Find how far an edge is from where it should be'''
        num = bitset.index(i)
        del bitset[num]
        return num

    # The values in DIVISIONS are all decreasing factors of 510935040
    # Which is the total number of edges permutations
    DIVISIONS = [42577920, 3870720, 387072, 43008, 5376, 768, 128]
    if end:
        # Only calculating last 7 edges
        # So a different section of the string is passed to reformat
        perm, index = reformat(state[5:12])
    else:
        perm, index = reformat(state[0:7])

    for i, z in enumerate(perm):
         index += get_num(int(z)) * DIVISIONS[i]

    return index

if __name__ == '__main__':
    import common
    cube = common.CUBE_INIT
    common.parse(cube, 'wyGr')

    import time
    s = time.time()

    for _ in range(100):
        hash(cube)
    print(time.time()-s)
