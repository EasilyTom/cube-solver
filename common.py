CUBE_INIT = [[[0, 0], [1, 0], [2, 0], [3, 0],[4, 0], [5, 0], [6, 0], [7, 0]], # Corners
                [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]], ''] # Edges, depth
# CUBE_INIT[0] is the corners array, in the order:
# wrb, wrg, wog, wob, yrb, yrg, yog, yob
# second value is which way its w/y sticker is facing wy ro bg 012
# CUBE_INIT[1] is the edges array, in the order:
# wr, wb, wo, wg, rb, bo, og, gr, yr, yb, yo, yg
# second value is which way axis its w/y (or r/o if it has neither) sticker is facing wy/ro/bg 012

# Cube_INIT[2] is the previous moves
def isSolved(cube):
    return cube[0:2] == [[[0, 0], [1, 0], [2, 0], [3, 0],[4, 0], [5, 0], [6, 0], [7, 0]],
                [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]]]

def parse(cube, string):
    '''Given a string representing a sequence of moves, execute them'''

    def res( _set,  direction):
        '''Rotate the relevant edge pieces when a cube face is turned'''
        if direction: # == if prime:
            cube[1][_set[0]], cube[1][_set[1]], cube[1][_set[2]], cube[1][_set[3]] = cube[1][_set[1]], cube[1][_set[2]], cube[1][_set[3]], cube[1][_set[0]]
        else:
            cube[1][_set[0]], cube[1][_set[1]], cube[1][_set[2]], cube[1][_set[3]] = cube[1][_set[3]], cube[1][_set[0]], cube[1][_set[1]], cube[1][_set[2]]
    def turn_white(cube, prime=False):
        # First deal with the edges
        res([0, 3, 2, 1], prime)

        for n in (0,1,2,3):
            if cube[0][n][1] != 0:
                cube[0][n][1] = 3 - cube[0][n][1]

        # Then the corners:
        # wrb -> wrg -> wog -> wob
        # prime: wob -> wog -> wrg -> wrb
        if prime:
            cube[0][0], cube[0][1], cube[0][2], cube[0][3] = cube[0][1], cube[0][2], cube[0][3], cube[0][0]
        else:
            cube[0][1], cube[0][2], cube[0][3], cube[0][0] = cube[0][0], cube[0][1], cube[0][2], cube[0][3]

    def turn_yellow(cube, prime=False):
        res([8, 9, 10, 11], prime)
        # yrb -> yob -> yog -> yrg
        for n in (4,5,6,7):
            if cube[0][n][1] != 0:
                cube[0][n][1] = 3 - cube[0][n][1]
        if prime:
            cube[0][4], cube[0][5], cube[0][6], cube[0][7] = cube[0][7], cube[0][4], cube[0][5], cube[0][6]
        else:
            cube[0][4], cube[0][5], cube[0][6], cube[0][7] = cube[0][5], cube[0][6], cube[0][7], cube[0][4]

    def turn_red(cube, prime=False):
        # The edges process is more complicated for red and orange
        res([0, 4, 8, 7], prime)
        for x in (0, 4, 8, 7):
            cube[1][x][1] = 1 - cube[1][x][1]

        for n in (0,1,4,5):
            if cube[0][n][1] != 1:
                cube[0][n][1] = 2 - cube[0][n][1]
        # wrb -> yrb -> yrg -> wrg
        if prime:
            cube[0][0], cube[0][4], cube[0][5], cube[0][1] = cube[0][4], cube[0][5], cube[0][1], cube[0][0]
        else:
            cube[0][0], cube[0][4], cube[0][5], cube[0][1] = cube[0][1], cube[0][0], cube[0][4], cube[0][5]

    def turn_orange(cube, prime=False):
        res([2, 6, 10, 5], prime)
        for x in [2, 6, 10, 5]:
            cube[1][x][1] = 1 - cube[1][x][1]
        for n in (2,3,6,7):
            if cube[0][n][1] != 1:
                cube[0][n][1] = 2 - cube[0][n][1]
        if prime:
            cube[0][2], cube[0][3], cube[0][6], cube[0][7] = cube[0][6], cube[0][2], cube[0][7], cube[0][3]
        else:
            cube[0][2], cube[0][3], cube[0][6], cube[0][7] = cube[0][3], cube[0][7], cube[0][2], cube[0][6]

    def turn_blue(cube, prime=False):
        res([1, 5, 9, 4], prime)
        for n in (0,3,4,7):
            if cube[0][n][1] != 2:
                cube[0][n][1] = 1 - cube[0][n][1]
        if prime:
            cube[0][0], cube[0][3], cube[0][4], cube[0][7] = cube[0][3], cube[0][7], cube[0][0], cube[0][4]
        else:
            cube[0][0], cube[0][3], cube[0][4], cube[0][7] = cube[0][4], cube[0][0], cube[0][7], cube[0][3]

    def turn_green(cube, prime=False):
        res([3, 7, 11, 6], prime)
        for n in (1,2,5,6):
            if cube[0][n][1] != 2:
                cube[0][n][1] = 1 - cube[0][n][1]
        if prime:
            cube[0][1], cube[0][2], cube[0][5], cube[0][6] = cube[0][5], cube[0][1], cube[0][6], cube[0][2]
        else:
            cube[0][1], cube[0][2], cube[0][5], cube[0][6] = cube[0][2], cube[0][6], cube[0][1], cube[0][5]


    MOVES = {'w': turn_white,
             'y': turn_yellow,
             'r': turn_red,
             'o': turn_orange,
             'b': turn_blue,
             'g': turn_green,
             }
    for i in string:
        MOVES[i.lower()](cube, i.islower())
        cube[2] += i

if __name__ == '__main__':
    print(CUBE_INIT)
    cube = CUBE_INIT
    parse(cube, 'w')
    print(cube)
