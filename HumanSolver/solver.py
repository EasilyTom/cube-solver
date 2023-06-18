def solve(cube):
    '''Generate a soloution to a scrambled cube.RubiksCube object'''
    cube.reset_moves() # set cube.move_list == []
    if cube.is_solved(): return [] # Prevents trying to solve a presolved cube
    # Each function is a stage of the begginers method of solving a cube
    _daisy(cube)
    _white_cross(cube)
    _white_corners(cube)
    _second_layer(cube)
    _yellow_cross(cube)
    _solve_cross(cube)
    _yellow_corners(cube)
    _yellow_rotations(cube)
    return cube.move_list


def _daisy(cube):
    """Create the daisy"""
    def find(colour, position, ignore=None):
        """Find the location of a colour

        Position should be either edge or corner, ignore denotes a face that
        shouldn't be checked

        Will return a list of touples (colour, y, x)
        """

        known_positions = []
        if position == 'corner':
            for y in [0, 2]:  # Checks all 4 corners on the face
                for x in [0, 2]:

                    if ignore != 'w' and cube.white[y][x] == colour:
                        known_positions.append(('w', y, x))

                    if ignore != 'y' and cube.yellow[y][x] == colour:
                        known_positions.append(('y', y, x))

                    if ignore != 'r' and cube.red[y][x] == colour:
                        known_positions.append(('r', y, x))

                    if ignore != 'o' and cube.orange[y][x] == colour:
                        known_positions.append(('o', y, x))

                    if ignore != 'b' and cube.blue[y][x] == colour:
                        known_positions.append(('b', y, x))

                    if ignore != 'g' and cube.green[y][x] == colour:
                        known_positions.append(('g', y, x))

        elif position == 'edge':

            EDGE_POSITIONS = [[0, 1], [1, 0], [1, 2], [2, 1]]
            for x in EDGE_POSITIONS:

                if ignore != 'w' and cube.white[x[0]][x[1]] == colour:
                    known_positions.append(('w', x[0], x[1]))

                if ignore != 'y' and cube.yellow[x[0]][x[1]] == colour:
                    known_positions.append(('y', x[0], x[1]))

                if ignore != 'r' and cube.red[x[0]][x[1]] == colour:
                    known_positions.append(('r', x[0], x[1]))

                if ignore != 'o' and cube.orange[x[0]][x[1]] == colour:
                    known_positions.append(('o', x[0], x[1]))

                if ignore != 'b' and cube.blue[x[0]][x[1]] == colour:
                    known_positions.append(('b', x[0], x[1]))

                if ignore != 'g' and cube.green[x[0]][x[1]] == colour:
                    known_positions.append(('g', x[0], x[1]))

        return known_positions

    white_edge_locations = find('w', 'edge')

    def perm_turn_yellow():
        '''Rotate the yellow face and update occupied_yellows accordingly'''
        cube.parse('Y')
        temp = occupied_yellows['r']
        occupied_yellows['r'] = occupied_yellows['g']
        occupied_yellows['g'] = occupied_yellows['o']
        occupied_yellows['o'] = occupied_yellows['b']
        occupied_yellows['b'] = temp

    occupied_yellows = {  # Key name refers to the colour of
                          # The face it borders,
                          # Not the edge stored there
        'r': False,
        'g': False,
        'b': False,
        'o': False
        }

    for i in range(4):  # Find which parts of the daisy are already completed
        if white_edge_locations[i][0] == 'y':
            y = white_edge_locations[i][1]
            x = white_edge_locations[i][2]
            if y == 0 and x == 1:
                occupied_yellows['r'] = True

            elif y == 1 and x == 0:
                occupied_yellows['g'] = True

            elif y == 1 and x == 2:
                occupied_yellows['b'] = True

            elif y == 2 and x == 1:
                occupied_yellows['o'] = True

    while not(occupied_yellows['r'] and occupied_yellows['g'] and
              occupied_yellows['b'] and occupied_yellows['o']):
        
        white_edge_locations = find('w', 'edge', 'y')
        face, y, x = white_edge_locations[0]
        if white_edge_locations[0][0] == 'w':
            # If it is on the white face,
            # move it above an empty yellow and move it down.
            if y == 0 and x == 1:
                if not occupied_yellows['o']:
                    cube.parse('OO')
                    occupied_yellows['o'] = True

                elif not occupied_yellows['b']:
                    cube.parse('WBB')
                    occupied_yellows['b'] = True

                elif not occupied_yellows['g']:
                    cube.parse('wGG')
                    occupied_yellows['g'] = True

                else:
                    cube.parse('WWRR')
                    occupied_yellows['r'] = True

            if y == 1 and x == 0:
                if not occupied_yellows['g']:
                    cube.parse('GG')
                    occupied_yellows['g'] = True

                elif not occupied_yellows['o']:
                    cube.parse('WOO')
                    occupied_yellows['o'] = True

                elif not occupied_yellows['r']:
                    cube.parse('wRR')
                    occupied_yellows['r'] = True

                else:
                    cube.parse('WWBB')
                    occupied_yellows['b'] = True

            if y == 1 and x == 2:
                if not occupied_yellows['b']:
                    cube.parse('BB')
                    occupied_yellows['b'] = True

                elif not occupied_yellows['r']:
                    cube.parse('WRR')
                    occupied_yellows['r'] = True

                elif not occupied_yellows['o']:
                    cube.parse('wOO')
                    occupied_yellows['o'] = True

                else:
                    cube.parse('WWGG')
                    occupied_yellows['g'] = True

            if y == 2 and x == 1:
                if not occupied_yellows['r']:
                    cube.parse('RR')
                    occupied_yellows['r'] = True

                elif not occupied_yellows['g']:
                    cube.parse('WGG')
                    occupied_yellows['g'] = True

                elif not occupied_yellows['b']:
                    cube.parse('wBB')
                    occupied_yellows['b'] = True

                else:
                    cube.parse('WWOO')
                    occupied_yellows['o'] = True

        else:
            # If it is on one of the other sides (not w/y)
            face_names = ['r', 'b', 'o', 'g']
            if y == 0:  # Top edge
                while 1:
                    # Rotate yellow until the space under the side is free
                    # Then move the yellow to there
                    if not occupied_yellows[face]:
                        # FDR'D'
                        right = face_names.index(face) + 1
                        if right > 3:
                            right = 0
                        cube.parse(face.upper()+'Y'+face_names[right]+'y')
                        occupied_yellows[face] = True
                        break

                    else:
                        perm_turn_yellow()

            elif y == 2: # Bottom edge
                while 1:
                    if not occupied_yellows[face]:
                        # F'DR'D'
                        right = face_names.index(face) + 1
                        if right > 3:
                            right = 0
                        cube.parse(face+'Y'+face_names[right]+'y')
                        occupied_yellows[face] = True
                        break
                    else:
                        perm_turn_yellow()

            elif y == 1 and x == 0: # Left edge
                left = face_names.index(face) - 1
                if left < 0:
                    left = 3
                while 1:
                    if not occupied_yellows[face_names[left]]:
                        cube.parse(face_names[left].upper())
                        occupied_yellows[face_names[left]] = True
                        break
                    else:
                        perm_turn_yellow()

            elif y == 1 and x == 2: # Right edge
                right = face_names.index(face) + 1
                if right > 3:
                    right = 0
                while 1:
                    if not occupied_yellows[face_names[right]]:
                        cube.parse(face_names[right])
                        occupied_yellows[face_names[right]] = True
                        break
                    else:
                        perm_turn_yellow()

def _white_cross(cube):
    """Move the white edges from yellow to the correct spots on white"""
    while 1:
        SIDES = {'r': cube.red[2][1],
                 'b': cube.blue[2][1],
                 'o': cube.orange[2][1],
                 'g': cube.green[2][1]
                 }
        YELLOWS = {'r': cube.yellow[0][1],
                   'b': cube.yellow[1][2],
                   'o': cube.yellow[2][1],
                   'g': cube.yellow[1][0]
                   }
        for colour in ['r', 'o', 'b', 'g']:
            # Check if any of the cubelets are in the right place
            if SIDES[colour] == colour and YELLOWS[colour] == 'w':
                cube.parse(colour.upper()*2) # Move cubelet from y to w face
         
        if (cube.white[0][1] == 'w'
            and cube.white[1][0] == 'w'
            and cube.white[1][2] == 'w'
            and cube.white[2][1] == 'w'):
            break # Done when all white edges in correct place
        cube.parse('Y')


def _white_corners(cube):
    '''Move white corners into correct place'''
    current = []

    def update_sides():
        '''Find the positions of each white corner'''
        nonlocal current
        current = []
        # Find the colours of the cubelets in each position
        wrb = (cube.white[2][2], cube.red[0][2], cube.blue[0][0])
        wrg = (cube.white[2][0], cube.red[0][0], cube.green[0][2])
        wob = (cube.white[0][2], cube.orange[0][0], cube.blue[0][2])
        wog = (cube.white[0][0], cube.orange[0][2], cube.green[0][0])
        yrb = (cube.yellow[0][2], cube.red[2][2], cube.blue[2][0])
        yrg = (cube.yellow[0][0], cube.red[2][0], cube.green[2][2])
        yob = (cube.yellow[2][2], cube.orange[2][0], cube.blue[2][2])
        yog = (cube.yellow[2][0], cube.orange[2][2], cube.green[2][0])
        corners = [wrb, wrg, wob, wog, yrb, yrg, yob, yog]

        for i, x in enumerate(corners):
            if 'w' in x:
                current.append(i)
            # current now contains the location of each white corner
    update_sides()

    def move_out(corner):
        # To move down we place the white corner in the top right
        # And do R'D'R

        def move(right):
            cube.parse(right.lower()+'y'+right.upper())

        if corner == 0:
            move('b')
        elif corner == 1:
            move('r')
        elif corner == 2:
            move('o')
        elif corner == 3:
            move('g')

    while 1:
        count = 0
        for x in range(4):
            if current[x] < 4: # if it is in one of the white corners
                while 1:
                    if current[x]+4 in current: # if the cubelet below is also a white
                        cube.parse('Y') # turn yellow and check again
                        update_sides()
                    else:
                        break
                move_out(current[x]) # otherwise move it down into the empty space
                count += 1
                update_sides()
        if count == 0: # If no whites have been moved, they must all be below
            break

    #  Now all the corners should be on the bottom
    
    def move_up(front, side):
        """Move a white from the bottom to where it needs to be"""
        # If bottom right FDF'
        # If bottom left F'D'F
        # If yellow, put on right F'DFDDF'D'F
        if side == 'right':
            cube.parse(front.upper()+'Y'+front.lower())
        elif side == 'left':
            cube.parse(front.lower()+'y'+front.upper())
        elif side == 'bottom':
            cube.parse(front.lower()+'Y'+front.upper()+'YY'+front.lower()
                       +'y'+front.upper())

    def stage_solved(cube):
        # Are all the corners in the correct places
        return (cube.red[0][0] == 'r' and cube.red[0][2] == 'r'
            and cube.blue[0][0] == 'b' and cube.blue[0][2] == 'b'
            and cube.orange[0][0] == 'o' and cube.orange[0][2] == 'o'
            and cube.green[0][0] == 'g' and cube.green[0][2] == 'g')
            
    while not stage_solved(cube):
        if (cube.red[2][2] in {'r', 'b', 'w'} and
                cube.blue[2][0] in {'r', 'b', 'w'} and
                cube.yellow[0][2] in {'r', 'b', 'w'}): # if wrb cubelet is below wrb
            if cube.red[2][2] == 'w': # Determine which sequence of moves need to be executed
                move_up('r', 'right') # And then do them
            elif cube.blue[2][0] == 'w':
                move_up('b', 'left')
            elif cube.yellow[0][2] == 'w':
                move_up('b', 'bottom')

        if (cube.red[2][0] in {'r', 'g', 'w'} and 
                cube.green[2][2] in {'r', 'g', 'w'} and
                cube.yellow[0][0] in {'r', 'g', 'w'}):
            if cube.red[2][0] == 'w':
                move_up('r', 'left')
            elif cube.green[2][2] == 'w':
                move_up('g', 'right')
            else:
                move_up('r', 'bottom')

        if (cube.orange[2][0] in {'o', 'b', 'w'} and
                cube.blue[2][2] in {'o', 'b', 'w'} and
                cube.yellow[2][2] in {'o', 'b', 'w'}):
            if cube.orange[2][0] == 'w':
                move_up('o', 'left')
            elif cube.blue[2][2] == 'w':
                move_up('b', 'right')
            else:
                move_up('o', 'bottom')

        if (cube.orange[2][2] in {'o', 'g', 'w'} and
                cube.green[2][0] in {'o', 'g', 'w'} and
                cube.yellow[2][0] in {'o', 'g', 'w'}):
            if cube.orange[2][2] == 'w':
                move_up('o', 'right')
            elif cube.green[2][0] == 'w':
                move_up('g', 'left')
            else:
                move_up('g', 'bottom')

        cube.parse('Y') # Turn yellow to create new pairings


def _second_layer(cube):
    """Solve the middle layer"""
    # To move from top to right do URU'R'U'F'UF
    # To move from top to left do U'L'ULUFU'F'
    def to_right(front):
        sides = ['r', 'g', 'o', 'b', 'r']
        right = sides[sides.index(front)+1]
        cube.parse('Y'+right.upper()+'y'+right.lower()+
                   'y'+front.lower()+'Y'+front.upper())

    def to_left(front):
        sides = ['r', 'g', 'o', 'b']
        left = sides[sides.index(front)-1]
        cube.parse('y'+left.lower()+'Y'+left.upper()+
                   'Y'+front.upper()+'y'+front.lower())

    # First deal with any that are in the right place but wrong way round
    def flip_side(side):
        to_right(side)
        cube.parse('YY')
        to_right(side)
        

    while 1:
        if cube.red[1][2] == 'b' and cube.blue[1][0] == 'r':
            flip_side('b')
        elif cube.blue[1][2] == 'o' and cube.orange[1][0] == 'b':
            flip_side('o')
        elif cube.orange[1][2] == 'g' and cube.green[1][0] == 'o':
            flip_side('g')
        elif cube.green[1][2] == 'r' and cube.red[1][0] == 'g':
            flip_side('r')
        else:
            break

    # Then deal with the rest
    while(cube.red[1] != ['r', 'r', 'r'] or
            cube.blue[1] != ['b', 'b', 'b'] or
            cube.orange[1] != ['o', 'o', 'o'] or
            cube.green[1] != ['g', 'g', 'g']):

        if ((cube.yellow[0][1] == 'y' or cube.red[2][1] == 'y') and
              (cube.yellow[1][2] == 'y' or cube.blue[2][1] == 'y') and
              (cube.yellow[1][0] == 'y' or cube.green[2][1] == 'y') and
              (cube.yellow[2][1] == 'y' or cube.orange[2][1] == 'y')):
            # If some of the edges are in eachother's spots, find them and move them
            if cube.red[1][0] != 'r':
                to_right('r')
            elif cube.blue[1][0] != 'b':
                to_right('b')
            elif cube.orange[1][0] != 'o':
                to_right('o')
            elif cube.green[1][0] != 'g':
                to_right('g')
            else:
                to_left('r')

        has_moved = False

        if cube.red[2][1] == 'r':
            if cube.yellow[0][1] == 'b':
                to_left('r')
                has_moved = True
            elif cube.yellow[0][1] == 'g':
                to_right('r')
                has_moved = True

        if cube.blue[2][1] == 'b':
            if cube.yellow[1][2] == 'o':
                to_left('b')
                has_moved = True
            elif cube.yellow[1][2] == 'r':
                to_right('b')
                has_moved = True

        if cube.orange[2][1] == 'o':
            if cube.yellow[2][1] == 'g':
                to_left('o')
                has_moved = True
            elif cube.yellow[2][1] == 'b':
                to_right('o')
                has_moved = True

        if cube.green[2][1] == 'g':
            if cube.yellow[1][0] == 'r':
                to_left('g')
                has_moved = True
            elif cube.yellow[1][0] == 'o':
                to_right('g')
                has_moved = True

        if not has_moved:
            cube.parse('y')

def _yellow_cross(cube):
    '''Create the yellow cross'''
    def solve_line(front):
        """Create a cross on the yellow face if there is a line
            front should be a side that has the line going from left to right
        """
        # FRUR'U'F'
        SIDES = ['r', 'g', 'o', 'b', 'r']
        right = SIDES[SIDES.index(front)+1]
        cube.parse(front.upper()+right.upper()+'Y'+
                   right.lower()+'y'+front.lower())

    def solve_L(front):
        """Create a cross on the yellow face if there is an L shape
            front should be the side where the yellow edges are on the far
            and left side
        """
        # FURU'R'F'
        SIDES = ['r', 'g', 'o', 'b', 'r']
        right = SIDES[SIDES.index(front)+1]
        cube.parse(front.upper()+'Y'+right.upper()+
                   'y'+right.lower()+front.lower())

    # Check if the cross is already there
    if (cube.yellow[0][1] == 'y' and
            cube.yellow[1][0] == 'y' and
            cube.yellow[1][2] == 'y'):
        return

    # Solve it if there's a dot
    if (cube.yellow[0][1] != 'y' and
          cube.yellow[1][0] != 'y' and
          cube.yellow[1][2] != 'y'):
        solve_line('g')
        solve_L('b')
        return

    # Solve if theres anything else
    if cube.yellow[0][1] == 'y':
        if cube.yellow[1][0] == 'y':
            solve_L('o')
        elif cube.yellow[1][2] == 'y':
            solve_L('g')
        else:
            solve_line('g')
    elif cube.yellow[1][2] == 'y':
        if cube.yellow[1][0] == 'y':
            solve_line('r')
        else:
            solve_L('r')
    else:
        solve_L('b')


def _solve_cross(cube):
    '''Move the edges of the cross so they are in the correct positions'''
    def solve_L(front):
        # RUUR'U'RU'R'U'
        SIDES = ['r', 'g', 'o', 'b', 'r']
        right = SIDES[SIDES.index(front)+1]
        cube.parse(right.upper()+'YY'+right.lower()+
                   'y'+right.upper()+'y'+right.lower()+'y')

    def solve_opposites(front):
        SIDES = ['r', 'g', 'o', 'b', 'r', 'g']
        right = SIDES[SIDES.index(front)+1]
        back = SIDES[SIDES.index(front)+2]
        solve_L(right)
        cube.parse('Y')
        solve_L(back)

    while 1:  # Rotates the yellow face until it is solveable
        count = 0
        if cube.red[2][1] == 'r':
            count += 1
        if cube.blue[2][1] == 'b':
            count += 1
        if cube.orange[2][1] == 'o':
            count += 1
        if cube.green[2][1] == 'g':
            count += 1

        if count == 2: # If it's solveable then continue
            break
        elif count == 4: # If it's already solved then move to next step
            return
        else:
            cube.parse('Y') # Otherwise turn it until one of the conditions is met

    # Determine which moves need to be executed to solve this stage
    if cube.red[2][1] == 'r':
        if cube.blue[2][1] == 'b':
            solve_L('g')
        elif cube.green[2][1] == 'g':
            solve_L('o')
        else:
            solve_opposites('g')
    elif cube.blue[2][1] == 'b':
        if cube.orange[2][1] == 'o':
            solve_L('r')
        else:
            solve_opposites('r')
    else:
        solve_L('b')


def _yellow_corners(cube):
    '''Move the yellow corners to the correct position'''
    
    def move_corners(front):
        """Corner permutation"""
        # L'URU'LUR'U'
        SIDES = ['r', 'g', 'o', 'b', 'r', 'b']
        right = SIDES[SIDES.index(front)+1]
        left = SIDES[SIDES.index(front)-1]
        cube.parse(left.lower()+'Y'+right.upper()+'y'+
                   left.upper()+'Y'+right.lower()+'y')

    while 1:
        # First need to find a corner which is in the correct position
        rb = {cube.yellow[0][2], cube.red[2][2], cube.blue[2][0]}
        bo = {cube.yellow[2][2], cube.orange[2][0], cube.blue[2][2]}
        og = {cube.yellow[2][0], cube.orange[2][2], cube.green[2][0]}
        gr = {cube.yellow[0][0], cube.red[2][0], cube.green[2][2]}
        if rb == {'r', 'b', 'y'}:
            if bo == {'o', 'b', 'y'}: # Check if it's already solved
                return
            move_corners('b')
            bo = {cube.yellow[2][2], cube.orange[2][0], cube.blue[2][2]}
            if bo == {'o', 'b', 'y'}: # Check if that has solved it
                return
            move_corners('b') # It must be solved now
            return

        if gr == {'r', 'g', 'y'}:
            if rb == {'r', 'b', 'y'}:
                return
            move_corners('r')
            rb = {cube.yellow[0][2], cube.red[2][2], cube.blue[2][0]}
            if rb == {'r', 'b', 'y'}:
                return
            move_corners('r')
            return

        if og == {'o', 'g', 'y'}:
            if gr == {'g', 'r', 'y'}:
                return
            move_corners('g')
            gr = {cube.yellow[0][0], cube.red[2][0], cube.green[2][2]}
            if gr == {'g', 'r', 'y'}:
                return
            move_corners('g')
            return

        if bo == {'o', 'b', 'y'}:
            if og == {'g', 'o', 'y'}:
                return
            move_corners('o')
            og = {cube.yellow[2][0], cube.orange[2][2], cube.green[2][0]}
            if og == {'g', 'o', 'y'}:
                return
            move_corners('o')
            return
        move_corners('r') # If there aren't any corners correct then move red
                            # and check again


def _yellow_rotations(cube):
    '''Rotate the yellow corners to the correct orientation'''
    def move(front):
        # RUUR'U'RU'R'L'UULUL'UL
        SIDES = ['r', 'g', 'o', 'b', 'r', 'b']
        right = SIDES[SIDES.index(front)+1]
        left = SIDES[SIDES.index(front)-1]
        cube.parse(right.upper()+'YY'+right.lower()+'y'+right.upper()+
                   'y'+right.lower()+left.lower()+'YY'+left.upper()+
                   'Y'+left.lower()+'Y'+left.upper())
    def headlights():
        # Check for headlight formations and solve them
        if cube.red[2] == ['y', 'r', 'y']:
            move('b')
        if cube.blue[2] == ['y', 'b', 'y']:
            move('o')
        if cube.orange[2] == ['y', 'o', 'y']:
            move('g')
        if cube.green[2] == ['y', 'g', 'y']:
            move('r')

    def perry():
        # Check for perry formations and solve them
        # They're called perrys because they looks like Perry the Platypus' eyes
        if cube.red[2][0] == 'y' and cube.orange[2][2] == 'y':
            move('r')
            move('r')
        if cube.blue[2][0] == 'y' and cube.green[2][2] == 'y':
            move('b')
            move('b')
        if cube.orange[2][0] == 'y' and cube.red[2][2] == 'y':
            move('o')
            move('o')
        if cube.green[2][0] == 'y' and cube.blue[2][2] == 'y':
            move('g')
            move('g')

    while not cube.is_solved():
        headlights()
        perry() 
        count = 0
        if cube.yellow[0][0] == 'y':
            count += 1
        if cube.yellow[0][2] == 'y':
            count += 1
        if cube.yellow[2][0] == 'y':
            count += 1
        if cube.yellow[2][2] == 'y':
            count += 1

        if count == 1:
            move('r') # This will break down fish formations

        if count == 2: # This deals with bowtie formations (two opposite corners solved)
            if 'y' in cube.red[2]:
                move('b')
            else:
                move('g')

if __name__ == '__main__':
    import cube
    for i in range(100001):
        arr = cube.RubiksCube()
        arr.scramble()
        solve(arr)
        if i % 1000 == 0:
            print(i)
