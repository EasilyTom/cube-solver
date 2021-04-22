def turn_white(cube, prime=False):
    # wrb -> wrg -> wog -> wob
    # prime: wob -> wog -> wrg -> wrb
    if prime:
        cube[0], cube[1], cube[2], cube[3] = cube[1], cube[2], cube[3], cube[0]
        for num in {1, 2, 3, 4}:
            corner = cube[num][1]
            if corner == 2: # red
                cube[num][1] = 4
            elif corner == 3: # orange
                cube[num][1] = 5
            elif corner == 4: # blue
                cube[num][1] = 3
            elif corner == 5: # green
                cube[num][1] = 2
    else:    
        cube[1], cube[2], cube[3], cube[0] = cube[0], cube[1], cube[2], cube[3]
        for num in {1, 2, 3, 4}:
            corner = cube[num][1]
            if corner == 2: # red
                cube[num][1] = 5
            elif corner == 3: # orange
                cube[num][1] = 4
            elif corner == 4: # blue
                cube[num][1] = 2
            elif corner == 5: # green
                cube[num][1] = 3
            
def turn_yellow(cube, prime=False):
    # yrb -> yob -> yog -> yrg
    if prime:
        cube[4], cube[5], cube[6], cube[7] = cube[7], cube[4], cube[5], cube[6]
        for num in {4, 5, 6, 7}:
            corner = cube[num][1]
            if corner == 2: # red
                cube[num][1] = 5
            elif corner == 3: # orange
                cube[num][1] = 4
            elif corner == 4: # blue
                cube[num][1] = 2
            elif corner == 5: # green
                cube[num][1] = 3
    else:
        cube[4], cube[5], cube[6], cube[7] = cube[5], cube[6], cube[7], cube[4]
        for num in {4, 5, 6, 7}:
            corner = cube[num][1]
            if corner == 2: # red
                cube[num][1] = 4
            elif corner == 3: # orange
                cube[num][1] = 5
            elif corner == 4: # blue
                cube[num][1] = 3
            elif corner == 5: # green
                cube[num][1] = 2
def turn_red(cube, prime=False):
    # wrb -> yrb -> yrg -> wrg
    if prime:
        cube[0], cube[4], cube[5], cube[1] = cube[4], cube[5], cube[1], cube[0]
        for num in {0, 1, 4, 5}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 5
            elif corner == 5: # green
                cube[num][1] = 1
            elif corner == 1: # yellow
                cube[num][1] = 4
            elif corner == 4: # blue
                cube[num][1] = 0
            
    else:
        cube[0], cube[4], cube[5], cube[1] = cube[1], cube[0], cube[4], cube[5]
        for num in {0, 1, 4, 5}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 4
            elif corner == 5: # green
                cube[num][1] = 0
            elif corner == 1: # yellow
                cube[num][1] = 5
            elif corner == 4: # blue
                cube[num][1] = 1

def turn_orange(cube, prime=False):
    if prime:
        cube[2], cube[3], cube[6], cube[7] = cube[6], cube[2], cube[7], cube[3]
        for num in {2, 3, 6, 7}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 4
            elif corner == 5: # green
                cube[num][1] = 0
            elif corner == 1: # yellow
                cube[num][1] = 5
            elif corner == 4: # blue
                cube[num][1] = 1
    else:
        cube[2], cube[3], cube[6], cube[7] = cube[3], cube[7], cube[2], cube[6]
        for num in {2, 3, 6, 7}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 5
            elif corner == 5: # green
                cube[num][1] = 1
            elif corner == 1: # yellow
                cube[num][1] = 4
            elif corner == 4: # blue
                cube[num][1] = 0

def turn_blue(cube, prime=False):
    if prime:
        cube[0], cube[3], cube[4], cube[7] = cube[3], cube[7], cube[0], cube[4]
        for num in {0, 3, 4, 7}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 2
            elif corner == 3: # orange
                cube[num][1] = 0
            elif corner == 1: # yellow
                cube[num][1] = 3
            elif corner == 2: # red
                cube[num][1] = 1
    else:
        cube[0], cube[3], cube[4], cube[7] = cube[4], cube[0], cube[7], cube[3]
        for num in {0, 3, 4, 7}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 3
            elif corner == 3: # orange
                cube[num][1] = 1
            elif corner == 1: # yellow
                cube[num][1] = 2
            elif corner == 2: # red
                cube[num][1] = 0

def turn_green(cube, prime=False):
    if prime:
        cube[1], cube[2], cube[5], cube[6] = cube[5], cube[1], cube[6], cube[2]
        for num in {1, 2, 5, 6}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 3
            elif corner == 3: # orange
                cube[num][1] = 1
            elif corner == 1: # yellow
                cube[num][1] = 2
            elif corner == 2: # red
                cube[num][1] = 0
    else:
        cube[1], cube[2], cube[5], cube[6] = cube[2], cube[6], cube[1], cube[5]
        for num in {1, 2, 5, 6}:
            corner = cube[num][1]
            if corner == 0: # white
                cube[num][1] = 2
            elif corner == 3: # orange
                cube[num][1] = 0
            elif corner == 1: # yellow
                cube[num][1] = 3
            elif corner == 2: # red
                cube[num][1] = 1
                
def parse(cube, string):
    MOVES = {'w': turn_white,
             'y': turn_yellow,
             'r': turn_red,
             'o': turn_orange,
             'b': turn_blue,
             'g': turn_green,
             }
    for i in string: 
        MOVES[i.lower()](cube, i.islower())
    cube[8][0] += 1
