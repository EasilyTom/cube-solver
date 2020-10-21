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
    #print(white_edge_locations)
                       
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
            occupied_yellows['blue'] != True or occupied_yellows['orange']):
        print('test')
        for side_being_processed in range(4):
            if white_edge_locations[side_being_processed][0] != 'yellow':
                # We need to move it to an empty location in yellow
                face, y, x = white_edge_locations[side_being_processed]
                print('t2')
                if white_edge_locations[side_being_processed][0] != 'white':
                    if y == 0 and x == 1:
                        # Top of the face
                        while 1:
                            print(face)
                            if occupied_yellows[face] == False:
                                #FRUR'FF
                                front = face_names.index(face)
    
                                if front == 3:
                                    left = 2
                                    right = 0
        
                                elif front == 0:
                                    left = 3
                                    right = 1

                                else:
                                    left = front - 1
                                    right = front + 1
                            
                                cube.turn_side_clockwise(face)
                                cube.turn_side_clockwise(face_names[right])
                                cube.turn_side_clockwise('white')
                                cube.turn_side_anti_clockwise(face_names[right])
                                cube.turn_side_clockwise(face)
                                cube.turn_side_clockwise(face)
                                occupied_yellows[face] = True
                                print('moved a side')
                                white_edge_locations = find('w', 'edge')
                                break
                            else:
                                cube.turn_side_anti_clockwise('white')
                                #need to change face
                                front = face_names.index(face)
    
                                if front == 3:
                                    face = face_names[0]
                                elif front == 0:
                                    face = face_names[3]
                                else:
                                    face = face_names[front+1]

                    elif y == 1 and x == 0:
                        #left side
                        front = face_names.index(face)
    
                        if front == 3:
                            left = 2
                            back = 1
                            right = 0

                        elif front == 2:
                            left = 1
                            back = 0
                            right = 3

                        elif front == 1:
                            left = 0
                            back = 3
                            right = 2

                        else:
                            left = 3
                            back = 2
                            right = 1
                            
                        if occupied_yellows[face_names[left]] == False:
                            cube.turn_side_clockwise(face_names[left])

                        else:
                            solved = False
                            for i in face_names:
                                if (occupied_yellows[i] == False and
                                        solved == False):
                                    solved = True
                                    empty_spot = abs(front - face_names.index(i))
                                    



                        


while 1:
    daisy()
    if (cube.red[0][1] == 'w' or cube.orange[0][1] == 'w' or
            cube.blue[0][1] == 'w' or cube.green[0][1] == 'w'):
       print('found error')
       break
    else:
        out_sides()
        cube.scramble()
        print('not found')






















