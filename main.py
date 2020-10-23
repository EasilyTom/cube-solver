from Cube import RubiksCube

cube = RubiksCube
cube.scramble()

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
                        #FBR'B'
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
                #F'BR'B'
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
                        

for x in range(10000):
    daisy()
    if(cube.yellow[0][1] != 'w' or cube.yellow[1][0] != 'w' or
       cube.yellow[1][2] != 'w' or cube.yellow[2][1] != 'w'):
        print('error found')
        break
    else:
        print('success', x)
        cube.scramble()






















