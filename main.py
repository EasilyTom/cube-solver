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
    print(white_edge_locations)
                       #top    left   right  bottom
    occupied_yellows = [False, False, False, False]
    
    for i in range(4): # Find which parts of the daisy are already completed
        if white_edge_locations[i][0] == 'yellow':
            y = white_edge_locations[i][1]
            x = white_edge_locations[i][2]
            if y == 0 and x == 1:
                occupied_yellows[0] = True

            elif y == 1 and x == 0:
                occupied_yellows[1] = True

            elif y == 1 and x == 2:
                occupied_yellows[2] = True

            elif y == 2 and x == 1:
                occupied_yellows[3] = True
            
    print(occupied_yellows)
        
    
    for side_being_processed in range(4):
        if white_edge_locations[side_being_processed][0] != 'yellow':
            # We need to move it to an empty location in yellow
            



daisy()
