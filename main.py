from Cube import RubiksCube

cube = RubiksCube
cube.scramble()

def solve():
    daisy()
    white_cross()
    white_corners()
    second_layer()
    
def out_sides():
    """Debugging. Print out each face"""
    
    print('\nwhite', cube.white)
    print('\nyellow', cube.yellow)
    print('\nred', cube.red)
    print('\norange', cube.orange)
    print('\nblue', cube.blue)
    print('\ngreen', cube.green)

def find(colour, position, ignore=None):
    """Find the location of a colour

    Position should be either edge or corner, ignore denotes a face that
    shouldn't be checked

    Will return a list of touples (colour, y, x)
    """

    known_positions = []
    if position == 'corner':
        for y in [0, 2]: # Checks all 4 corners on the face
            for x in [0,2]:
                
                if ignore != 'white' and cube.white[y][x] == colour:
                        known_positions.append(('white', y, x))

                if ignore != 'yellow' and cube.yellow[y][x] == colour:
                        known_positions.append(('yellow', y, x))
                
                if ignore != 'red' and cube.red[y][x] == colour:
                        known_positions.append(('red', y, x))

                if ignore != 'orange' and cube.orange[y][x] == colour:
                        known_positions.append(('orange', y, x))
                           
                if ignore != 'blue' and cube.blue[y][x] == colour:
                        known_positions.append(('blue', y, x))

                if ignore != 'green' and cube.green[y][x] == colour:
                        known_positions.append(('green', y, x))

    elif position == 'edge':
        
        edge_positions = [[0,1],[1,0],[1,2],[2,1]]
        for x in edge_positions:
            
            if ignore != 'white' and cube.white[x[0]][x[1]] == colour:
                known_positions.append(('white', x[0], x[1]))

            if ignore != 'yellow' and cube.yellow[x[0]][x[1]] == colour:
                known_positions.append(('yellow', x[0], x[1]))

            if ignore != 'red' and cube.red[x[0]][x[1]] == colour:
                known_positions.append(('red', x[0], x[1]))

            if ignore != 'orange' and cube.orange[x[0]][x[1]] == colour:
                known_positions.append(('orange', x[0], x[1]))

            if ignore != 'blue' and cube.blue[x[0]][x[1]] == colour:
                known_positions.append(('blue', x[0], x[1]))

            if ignore != 'green' and cube.green[x[0]][x[1]] == colour:
                known_positions.append(('green', x[0], x[1]))
            
    return known_positions



                
def daisy():
    """Create the daisy"""
    white_edge_locations = find('w', 'edge')

    def perm_turn_yellow():
        cube.turn_side_clockwise('yellow')
        temp = occupied_yellows['red']
        occupied_yellows['red'] = occupied_yellows['green']
        occupied_yellows['green'] = occupied_yellows['orange']
        occupied_yellows['orange'] = occupied_yellows['blue']
        occupied_yellows['blue'] = temp

    def double_turn(side):
        cube.turn_side_clockwise(side)
        cube.turn_side_clockwise(side)
        occupied_yellows[side] = True
                       
    occupied_yellows = { # Key name refers to the colour of the face it borders
                         # Not the edge stored there
        'red': False,
        'green': False,
        'blue': False,
        'orange': False
        }

    for i in range(4): # Find which parts of the daisy are already completed
        if white_edge_locations[i][0] == 'yellow':
            y = white_edge_locations[i][1]
            x = white_edge_locations[i][2]
            if y == 0 and x == 1:
                occupied_yellows['red'] = True

            elif y == 1 and x == 0:
                occupied_yellows['green'] = True

            elif y == 1 and x == 2:
                occupied_yellows['blue'] = True

            elif y == 2 and x == 1:
                occupied_yellows['orange'] = True
        
    face_names = ['red', 'blue', 'orange', 'green']
    while(occupied_yellows['red'] != True or occupied_yellows['green'] != True or
            occupied_yellows['blue'] != True or occupied_yellows['orange'] != True):
        white_edge_locations = find('w', 'edge', 'yellow')
        face, y, x = white_edge_locations[0]
        if white_edge_locations[0][0] == 'white':
            if y == 0 and x == 1:
                if occupied_yellows['orange'] == False:
                    double_turn('orange')
                
                elif occupied_yellows['blue'] == False:
                    cube.turn_side_clockwise('white')
                    double_turn('blue')

                elif occupied_yellows['green'] == False:
                    cube.turn_side_anti_clockwise('white')
                    double_turn('green')

                else:
                    cube.turn_side_clockwise('white')
                    cube.turn_side_clockwise('white')
                    double_turn('red')

            if y == 1 and x == 0:
                if occupied_yellows['green'] == False:
                    double_turn('green')
                    
                elif occupied_yellows['orange'] == False:
                    cube.turn_side_clockwise('white')
                    double_turn('orange')

                elif occupied_yellows['red'] == False:
                    cube.turn_side_anti_clockwise('white')
                    double_turn('red')

                else:
                    cube.turn_side_clockwise('white')
                    cube.turn_side_clockwise('white')
                    double_turn('blue')

            if y == 1 and x ==2:
                if occupied_yellows['blue'] == False:
                    double_turn('blue')
                    
                elif occupied_yellows['red'] == False:
                    cube.turn_side_clockwise('white')
                    double_turn('red')
                    
                elif occupied_yellows['orange'] == False:
                    cube.turn_side_anti_clockwise('white')
                    double_turn('orange')

                else:
                    cube.turn_side_clockwise('white')
                    cube.turn_side_clockwise('white')
                    double_turn('green')

            if y == 2 and x == 1:
                if occupied_yellows['red'] == False:
                    double_turn('red')
                    
                elif occupied_yellows['green'] == False:
                    cube.turn_side_clockwise('white')
                    double_turn('green')

                elif occupied_yellows['blue'] == False:
                    cube.turn_side_anti_clockwise('white')
                    double_turn('blue')

                else:
                    cube.turn_side_clockwise('white')
                    cube.turn_side_clockwise('white')
                    double_turn('orange')

        else:
            if y == 0: # Top edge
                while 1:
                    if occupied_yellows[face] == False:
                        #FDR'D'
                        right = face_names.index(face) + 1
                        if right > 3:
                            right = 0
                            
                        cube.turn_side_clockwise(face)
                        cube.turn_side_clockwise('yellow')
                        cube.turn_side_anti_clockwise(face_names[right])
                        cube.turn_side_anti_clockwise('yellow')
                        occupied_yellows[face] = True
                        break
                    
                    else:
                        perm_turn_yellow()

            elif y == 2:
                #F'DR'D'
                right = face_names.index(face) + 1
                if right > 3:
                    right = 0
                cube.turn_side_anti_clockwise(face)
                cube.turn_side_clockwise('yellow')
                cube.turn_side_anti_clockwise(face_names[right])
                cube.turn_side_anti_clockwise('yellow')
                occupied_yellows[face] = True

            elif y == 1 and x == 0:
                left = face_names.index(face) - 1
                if left < 0:
                    left = 3
                while 1:
                    if occupied_yellows[face_names[left]] == False:
                        cube.turn_side_clockwise(face_names[left])
                        occupied_yellows[face_names[left]] = True
                        break
                    else:
                        perm_turn_yellow()

            elif y == 1 and x == 2:
                right = face_names.index(face) + 1
                if right > 3:
                    right = 0
                while 1:
                    if occupied_yellows[face_names[right]] == False:
                        cube.turn_side_anti_clockwise(face_names[right])
                        occupied_yellows[face_names[right]] = True
                        break
                    else:
                        perm_turn_yellow()
                        
    
def white_cross():
    """Move the white edges from yellow to the correct spots on white"""
    def move_up(colour):
        names = {'r': 'red',
                 'b': 'blue',
                 'o': 'orange',
                 'g': 'green'
                 }
        
        
        while 1:
            sides = {'r': cube.red[2][1],
                     'b': cube.blue[2][1],
                     'o': cube.orange[2][1],
                     'g': cube.green[2][1]
                     }
            yellows = {'r': cube.yellow[0][1],
                       'b': cube.yellow[1][2],
                       'o': cube.yellow[2][1],
                       'g': cube.yellow[1][0]
                       }
            if sides[colour] == colour and yellows[colour] == 'w':
                cube.turn_side_clockwise(names[colour])
                cube.turn_side_clockwise(names[colour])
                break
            else:
                cube.turn_side_clockwise('yellow')
    move_up('r')
    move_up('b')
    move_up('o')
    move_up('g')


def white_corners():
    current = []
    rotation = []
    def update_sides():
        nonlocal current, rotation
        current = []
        rotation = []
        wrb = (cube.white[2][2], cube.red[0][2], cube.blue[0][0])
        wrg = (cube.white[2][0], cube.red[0][0], cube.green[0][2])
        wob = (cube.white[0][2], cube.orange[0][0], cube.blue[0][2])
        wog = (cube.white[0][0], cube.orange[0][2], cube.green[0][0])
        yrb = (cube.yellow[0][2], cube.red[2][2], cube.blue[2][0])
        yrg = (cube.yellow[0][0], cube.red[2][0], cube.green[2][2])
        yob = (cube.yellow[2][2], cube.orange[2][0], cube.blue[2][2])
        yog = (cube.yellow[2][0], cube.orange[2][2], cube.green[2][0])
        corners  = [wrb, wrg, wob, wog, yrb, yrg, yob, yog]
    
        for x in range(8):
            for i in range(3):
                if corners[x][i] == 'w':
                    current.append(x)
                    break
    update_sides()
    def move_out(corner):
        can_move = True
        while 1:
            for x in range(4):
                if corner + 4 == current[x]:
                    can_move == False
            if can_move == True:
                break
            else:
                cube.rotate_side_clockwise('yellow')
                for x in range(4):
                    if current[x] == 4:
                        current[x] == 6
                    elif current[x] == 5:
                        current[x] = 4
                    elif current[x] == 6:
                        current[x] = 7
                    elif current[x] == 7:
                        current[x] = 5
        # To move down we place the white corner in the top right
        # And do R'D'R
        def move(right):
            cube.turn_side_anti_clockwise(right)
            cube.turn_side_anti_clockwise('yellow')
            cube.turn_side_clockwise(right)

        if corner == 0:
            move('blue')
        elif corner == 1:
            move('red')
        elif corner == 2:
            move('orange')
        elif corner == 3:
            move('green')
        else:
            return True
            

    while 1:
        count = 0
        for x in range(4):
            if current[x] < 4:
                while 1:
                    if current[x]+4 in current:
                        cube.turn_side_clockwise('yellow')
                        update_sides()
                    else:
                        break
                move_out(current[x])
                count += 1
                update_sides()
        if count == 0:
            break
    
    def move_up(front, side):
        """Move a white from the bottom to where it needs to be"""
        # If bottom right FDF'
        # If bottom left F'D'F
        # If yellow, put on right F'DFDDF'D'F
        if side == 'right':
            cube.turn_side_clockwise(front)
            cube.turn_side_clockwise('yellow')
            cube.turn_side_anti_clockwise(front)
        elif side == 'left':
            cube.turn_side_anti_clockwise(front)
            cube.turn_side_anti_clockwise('yellow')
            cube.turn_side_clockwise(front)
        elif side == 'bottom':
            cube.turn_side_anti_clockwise(front)
            cube.turn_side_clockwise('yellow')
            cube.turn_side_clockwise(front)
            cube.turn_side_clockwise('yellow')
            cube.turn_side_clockwise('yellow')
            cube.turn_side_anti_clockwise(front)
            cube.turn_side_anti_clockwise('yellow')
            cube.turn_side_clockwise(front)

    # Now all the corners should either be on the bottom
    
    while not(cube.red[0][2] == 'r' and cube.blue[0][0] == 'b'):
        if (cube.red[2][2] in ['r','b','w'] and
            cube.blue[2][0] in ['r','b','w'] and
            cube.yellow[0][2] in ['r','b','w']):
            if cube.red[2][2] == 'w':
                move_up('red', 'right')
            elif cube.blue[2][0] == 'w':
                move_up('blue', 'left')
            elif cube.yellow[0][2] == 'w':
                move_up('blue', 'bottom')
        else:
            cube.turn_side_clockwise('yellow')
    
    while not(cube.red[0][0] == 'r' and cube.green[0][2] == 'g'):
        if (cube.red[2][0] in ['r','g','w'] and
            cube.green[2][2] in ['r','g','w'] and
            cube.yellow[0][0] in ['r','g','w']):
            if cube.red[2][0] == 'w':
                move_up('red', 'left')
            elif cube.green[2][2] == 'w':
                move_up('green', 'right')
            else:
                move_up('red', 'bottom')
        else:
            cube.turn_side_clockwise('yellow')
    
    while not(cube.orange[0][0] == 'o' and cube.blue[0][2] == 'b'):
        if (cube.orange[2][0] in ['o','b','w'] and
            cube.blue[2][2] in ['o','b','w'] and
            cube.yellow[2][2] in ['o','b','w']):
            if cube.orange[2][0] == 'w':
                move_up('orange', 'left')
            elif cube.blue[2][2] == 'w':
                move_up('blue', 'right')
            else:
                move_up('orange', 'bottom')
        else:
            cube.turn_side_clockwise('yellow')
    
    while not(cube.orange[0][2] == 'o' and cube.green[0][0] == 'g'):
        if (cube.orange[2][2] in ['o','g','w'] and
            cube.green[2][0] in ['o','g','w'] and
            cube.yellow[2][0] in ['o','g','w']):
            if cube.orange[2][2] == 'w':
                move_up('orange', 'right')
            elif cube.green[2][0] == 'w':
                move_up('green', 'left')
            else:
                move_up('green', 'bottom')
        else:
            cube.turn_side_clockwise('yellow')

def second_layer():
    """Solve the middle layer"""
    # To move from top to right do URU'R'U'F'UF
    # To move from top to left do U'L'ULUFU'F'
    def to_right(front):
        sides = ['red', 'green', 'orange', 'blue', 'red']
        right = sides[sides.index(front)+1]
        cube.turn_side_clockwise('yellow')
        cube.turn_side_clockwise(right)
        cube.turn_side_anti_clockwise('yellow')
        cube.turn_side_anti_clockwise(right)
        cube.turn_side_anti_clockwise('yellow')
        cube.turn_side_anti_clockwise(front)
        cube.turn_side_clockwise('yellow')
        cube.turn_side_clockwise(front)

    def to_left(front):
        sides = ['red', 'green', 'orange', 'blue']
        left = sides[sides.index(front)-1]
        cube.turn_side_anti_clockwise('yellow')
        cube.turn_side_anti_clockwise(left)
        cube.turn_side_clockwise('yellow')
        cube.turn_side_clockwise(left)
        cube.turn_side_clockwise('yellow')
        cube.turn_side_clockwise(front)
        cube.turn_side_anti_clockwise('yellow')
        cube.turn_side_anti_clockwise(front)
        
    
    # First deal with any that are in the right place but wrong way round
    def flip_side(side):
        cube.turn_side_anti_clockwise('yellow')
        to_right(side)
        cube.turn_side_anti_clockwise('yellow')
        cube.turn_side_anti_clockwise('yellow')
        to_right(side)
        
    while 1:
        if cube.red[1][2] == 'b' and cube.blue[1][0] == 'r':
            flip_side('blue')
        elif cube.blue[1][2] == 'o' and cube.orange[1][0] == 'b':
            flip_side('orange')
        elif cube.orange[1][2] == 'g' and cube.green[1][0] == 'o':
            flip_side('green')
        elif cube.green[1][2] == 'r' and cube.red[1][0] == 'g':
            flip_side('red')
        else:
            break       

    while(cube.red[1] != ['r', 'r', 'r'] or
              cube.blue[1] != ['b', 'b', 'b'] or
              cube.orange[1] != ['o', 'o', 'o'] or
              cube.green[1] != ['g', 'g', 'g']):

        if ((cube.yellow[0][1] == 'y' or cube.red[2][1] == 'y') and
            (cube.yellow[1][2] == 'y' or cube.blue[2][1] == 'y') and
            (cube.yellow[1][0] == 'y' or cube.green[2][1] == 'y') and
            (cube.yellow[2][1] == 'y' or cube.orange[2][1] == 'y')):

            if cube.red[1][0] != 'r':
                to_right('red')
            elif cube.blue[1][0] != 'b':
                to_right('blue')
            elif cube.orange[1][0] != 'o':
                to_right('orange')
            elif cube.green[1][0] != 'g':
                to_right('green')
            else:
                to_left('red')
                
        
        has_moved = False

        if cube.red[2][1] == 'r':
            if cube.yellow[0][1] == 'b':
                to_left('red')
                has_moved = True
            elif cube.yellow[0][1] == 'g':
                to_right('red')
                has_moved = True

        if cube.blue[2][1] == 'b':
            if cube.yellow[1][2] == 'o':
                to_left('blue')
                has_moved = True
            elif cube.yellow[1][2] == 'r':
                to_right('blue')
                has_moved = True

        if cube.orange[2][1] == 'o':
            if cube.yellow[2][1] == 'g':
                to_left('orange')
                has_moved = True
            elif cube.yellow[2][1] == 'b':
                to_right('orange')
                has_moved = True

        if cube.green[2][1] == 'g':
            if cube.yellow[1][0] == 'r':
                to_left('green')
                has_moved = True
            elif cube.yellow[1][0] == 'o':
                to_right('green')
                has_moved = True
        
        if has_moved == False:
            cube.turn_side_clockwise('yellow')
          
        
solve()
