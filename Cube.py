import random

class RubiksCube:
        # Creates  2D arrays for each side
        #  W
        # GRBO
        #  Y
                  #o
    white = [['w','w','w'],
             ['w','w','w'],
             ['w','w','w']]

                #w
    red = [['r','r','r'],
           ['r','r','r'],
           ['r','r','r']]

                   #w
    orange = [['o','o','o'],
              ['o','o','o'],
              ['o','o','o']]
    
                  #w
    green = [['g','g','g'],
             ['g','g','g'],
             ['g','g','g']]
    
                 #w
    blue = [['b','b','b'],
            ['b','b','b'],
            ['b','b','b']]

                   #r
    yellow = [['y','y','y'],
              ['y','y','y'],
              ['y','y','y']]

    def turn_side_clockwise(side):
        """Turn a side in the clockwise direction"""
        # Sorry PEP8
        # The long lines of code move the edges of the face around
        if side == 'white':
            RubiksCube.white = [list(r) for r in zip(*RubiksCube.white[::-1])]
            # b -> r -> g -> o
            RubiksCube.blue[0], RubiksCube.red[0], RubiksCube.green[0], RubiksCube.orange[0] = RubiksCube.orange[0], RubiksCube.blue[0], RubiksCube.red[0], RubiksCube.green[0]

        elif side == 'yellow':
            RubiksCube.yellow = [list(r) for r in zip(*RubiksCube.yellow[::-1])]
            # b-> o -> g -> r
            RubiksCube.blue[2], RubiksCube.red[2], RubiksCube.green[2], RubiksCube.orange[2] = RubiksCube.red[2], RubiksCube.green[2], RubiksCube.orange[2], RubiksCube.blue[2]
            
        elif side == 'red':
            RubiksCube.red = [list(r) for r in zip(*RubiksCube.red[::-1])]
            # w -> b -> y -> g
            RubiksCube.white[2][0], RubiksCube.blue[0][0], RubiksCube.yellow[0][2], RubiksCube.green[2][2] = RubiksCube.green[2][2], RubiksCube.white[2][0], RubiksCube.blue[0][0], RubiksCube.yellow[0][2]
            RubiksCube.white[2][1], RubiksCube.blue[1][0], RubiksCube.yellow[0][1], RubiksCube.green[1][2] = RubiksCube.green[1][2], RubiksCube.white[2][1], RubiksCube.blue[1][0], RubiksCube.yellow[0][1]
            RubiksCube.white[2][2], RubiksCube.blue[2][0], RubiksCube.yellow[0][0], RubiksCube.green[0][2] = RubiksCube.green[0][2], RubiksCube.white[2][2], RubiksCube.blue[2][0], RubiksCube.yellow[0][0]
            
        elif side == 'orange':
            RubiksCube.orange = [list(r) for r in zip(*RubiksCube.orange[::-1])]
            # w -> g -> y -> b
            RubiksCube.white[0][2], RubiksCube.green[0][0], RubiksCube.yellow[2][0], RubiksCube.blue[2][2] = RubiksCube.blue[2][2], RubiksCube.white[0][2], RubiksCube.green[0][0], RubiksCube.yellow[2][0]
            RubiksCube.white[0][1], RubiksCube.green[1][0], RubiksCube.yellow[2][1], RubiksCube.blue[1][2] = RubiksCube.blue[1][2], RubiksCube.white[0][1], RubiksCube.green[1][0], RubiksCube.yellow[2][1]
            RubiksCube.white[0][0], RubiksCube.green[2][0], RubiksCube.yellow[2][2], RubiksCube.blue[0][2] = RubiksCube.blue[0][2], RubiksCube.white[0][0], RubiksCube.green[2][0], RubiksCube.yellow[2][2]
            
        elif side == 'blue':
            RubiksCube.blue = [list(r) for r in zip(*RubiksCube.blue[::-1])]
            # w -> o -> y -> r
            RubiksCube.white[0][2], RubiksCube.orange[2][0], RubiksCube.yellow[0][2], RubiksCube.red[0][2] = RubiksCube.red[0][2], RubiksCube.white[0][2], RubiksCube.orange[2][0], RubiksCube.yellow[0][2]
            RubiksCube.white[1][2], RubiksCube.orange[1][0], RubiksCube.yellow[1][2], RubiksCube.red[1][2] = RubiksCube.red[1][2], RubiksCube.white[1][2], RubiksCube.orange[1][0], RubiksCube.yellow[1][2]
            RubiksCube.white[2][2], RubiksCube.orange[0][0], RubiksCube.yellow[2][2], RubiksCube.red[2][2] = RubiksCube.red[2][2], RubiksCube.white[2][2], RubiksCube.orange[0][0], RubiksCube.yellow[2][2]
            
        elif side == 'green':
            RubiksCube.green = [list(r) for r in zip(*RubiksCube.green[::-1])]
            # w -> r -> y -> o
            RubiksCube.white[0][0], RubiksCube.red[0][0], RubiksCube.yellow[0][0], RubiksCube.orange[2][2] = RubiksCube.orange[2][2], RubiksCube.white[0][0], RubiksCube.red[0][0], RubiksCube.yellow[0][0]
            RubiksCube.white[1][0], RubiksCube.red[1][0], RubiksCube.yellow[1][0], RubiksCube.orange[1][2] = RubiksCube.orange[1][2], RubiksCube.white[1][0], RubiksCube.red[1][0], RubiksCube.yellow[1][0]
            RubiksCube.white[2][0], RubiksCube.red[2][0], RubiksCube.yellow[2][0], RubiksCube.orange[0][2] = RubiksCube.orange[0][2], RubiksCube.white[2][0], RubiksCube.red[2][0], RubiksCube.yellow[2][0]

    def turn_side_anti_clockwise(side):
        """Turn side in the anticlockwise direction"""
        if side == 'white':
            RubiksCube.white = [list(r) for r in zip(*RubiksCube.white)][::-1]
            # b -> o -> g -> r
            RubiksCube.blue[0], RubiksCube.red[0], RubiksCube.green[0], RubiksCube.orange[0] = RubiksCube.red[0], RubiksCube.green[0], RubiksCube.orange[0], RubiksCube.blue[0]
            
        elif side == 'yellow':
            RubiksCube.yellow = [list(r) for r in zip(*RubiksCube.yellow)][::-1]
            # b -> r -> g -> o
            RubiksCube.blue[2], RubiksCube.red[2], RubiksCube.green[2], RubiksCube.orange[2] = RubiksCube.orange[2], RubiksCube.blue[2], RubiksCube.red[2], RubiksCube.green[2]
            
        elif side == 'red':
            RubiksCube.red = [list(r) for r in zip(*RubiksCube.red)][::-1]
            # w -> g -> y -> b
            RubiksCube.white[2][0], RubiksCube.blue[0][0], RubiksCube.yellow[0][2], RubiksCube.green[2][2] = RubiksCube.blue[0][0], RubiksCube.yellow[0][2], RubiksCube.green[2][2], RubiksCube.white[2][0]
            RubiksCube.white[2][1], RubiksCube.blue[1][0], RubiksCube.yellow[0][1], RubiksCube.green[1][2] = RubiksCube.blue[1][0], RubiksCube.yellow[0][1], RubiksCube.green[1][2], RubiksCube.white[2][1]
            RubiksCube.white[2][2], RubiksCube.blue[2][0], RubiksCube.yellow[0][0], RubiksCube.green[0][2] = RubiksCube.blue[2][0], RubiksCube.yellow[0][0], RubiksCube.green[0][2], RubiksCube.white[2][2]
            
        elif side == 'orange':
            RubiksCube.orange = [list(r) for r in zip(*RubiksCube.orange)][::-1]
            # w -> b -> y -> g
            RubiksCube.white[0][2], RubiksCube.green[0][0], RubiksCube.yellow[2][0], RubiksCube.blue[2][2] = RubiksCube.green[0][0], RubiksCube.yellow[2][0], RubiksCube.blue[2][2], RubiksCube.white[0][2]
            RubiksCube.white[0][1], RubiksCube.green[1][0], RubiksCube.yellow[2][1], RubiksCube.blue[1][2] = RubiksCube.green[1][0], RubiksCube.yellow[2][1], RubiksCube.blue[1][2], RubiksCube.white[0][1] 
            RubiksCube.white[0][0], RubiksCube.green[2][0], RubiksCube.yellow[2][2], RubiksCube.blue[0][2] = RubiksCube.green[2][0], RubiksCube.yellow[2][2], RubiksCube.blue[0][2], RubiksCube.white[0][0]
            
        elif side == 'blue':
            RubiksCube.blue = [list(r) for r in zip(*RubiksCube.blue)][::-1]
            # w -> r -> y -> o
            RubiksCube.white[0][2], RubiksCube.orange[2][0], RubiksCube.yellow[0][2], RubiksCube.red[0][2] = RubiksCube.orange[2][0], RubiksCube.yellow[0][2], RubiksCube.red[0][2], RubiksCube.white[0][2]
            RubiksCube.white[1][2], RubiksCube.orange[1][0], RubiksCube.yellow[1][2], RubiksCube.red[1][2] = RubiksCube.orange[1][0], RubiksCube.yellow[1][2], RubiksCube.red[1][2], RubiksCube.white[1][2]
            RubiksCube.white[2][2], RubiksCube.orange[0][0], RubiksCube.yellow[2][2], RubiksCube.red[2][2] = RubiksCube.orange[0][0], RubiksCube.yellow[2][2], RubiksCube.red[2][2], RubiksCube.white[2][2]
            
        elif side == 'green':
            RubiksCube.green = [list(r) for r in zip(*RubiksCube.green)][::-1]
            # w -> o -> y -> r
            RubiksCube.white[0][0], RubiksCube.red[0][0], RubiksCube.yellow[0][0], RubiksCube.orange[2][2] = RubiksCube.red[0][0], RubiksCube.yellow[0][0], RubiksCube.orange[2][2], RubiksCube.white[0][0]
            RubiksCube.white[1][0], RubiksCube.red[1][0], RubiksCube.yellow[1][0], RubiksCube.orange[1][2] = RubiksCube.red[1][0], RubiksCube.yellow[1][0], RubiksCube.orange[1][2], RubiksCube.white[1][0]
            RubiksCube.white[2][0], RubiksCube.red[2][0], RubiksCube.yellow[2][0], RubiksCube.orange[0][2] = RubiksCube.red[2][0], RubiksCube.yellow[2][0], RubiksCube.orange[0][2], RubiksCube.white[2][0]

    def check_if_solved():
        """Check if the cube is in a solved state"""
        for x in range(0,3):
            for y in range (0,3):
                if (
                        RubiksCube.white[x][y] != 'w' or
                        RubiksCube.yellow[x][y] != 'y' or
                        RubiksCube.red[x][y] != 'r' or
                        RubiksCube.orange[x][y] != 'o' or
                        RubiksCube.blue[x][y] != 'b' or
                        RubiksCube.green[x][y] != 'g'
                        ):
                    return False
        return True

    def scramble():
        """Randomise the cube"""
        colours = ['white', 'white', 'yellow', 'yellow', 'red', 'red',
                   'orange', 'orange', 'blue', 'blue', 'green', 'green']
        for _ in range(random.randint(80,120)):
            x = random.randint(0,11) # Even moves clockwise odd moves anti           
            if x % 2 == 0:
                RubiksCube.turn_side_clockwise(colours[x])
            else:
                RubiksCube.turn_side_anti_clockwise(colours[x])

    def reset():
        white = [['w','w','w'],
                 ['w','w','w'],
                 ['w','w','w']]

        red = [['r','r','r'],
               ['r','r','r'],
               ['r','r','r']]

        orange = [['o','o','o'],
                  ['o','o','o'],
                  ['o','o','o']]
    
        green = [['g','g','g'],
                 ['g','g','g'],
                 ['g','g','g']]
    
        blue = [['b','b','b'],
                ['b','b','b'],
                ['b','b','b']]

        yellow = [['y','y','y'],
                  ['y','y','y'],
                  ['y','y','y']]
