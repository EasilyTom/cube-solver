import random


class RubiksCube:

    def __init__(self):
        None
        
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

    def turn_side_clockwise(self, side):
        """Turn a side in the clockwise direction"""
        # Sorry PEP8
        # The long lines of code move the edges of the face around
        if side == 'white':
            self.white = [list(r) for r in zip(*self.white[::-1])]
            # b -> r -> g -> o
            self.blue[0], self.red[0], self.green[0], self.orange[0] = self.orange[0], self.blue[0], self.red[0], self.green[0]

        elif side == 'yellow':
            self.yellow = [list(r) for r in zip(*self.yellow[::-1])]
            # b-> o -> g -> r
            self.blue[2], self.red[2], self.green[2], self.orange[2] = self.red[2], self.green[2], self.orange[2], self.blue[2]
            
        elif side == 'red':
            self.red = [list(r) for r in zip(*self.red[::-1])]
            # w -> b -> y -> g
            for i in range(3):
                self.white[2][i], self.blue[i][0], self.yellow[0][2-i], self.green[2-i][2] = self.green[2-i][2], self.white[2][i], self.blue[i][0], self.yellow[0][2-i]
            
        elif side == 'orange':
            self.orange = [list(r) for r in zip(*self.orange[::-1])]
            # w -> g -> y -> b
            for i in range(3):
                self.white[0][2-i], self.green[i][0], self.yellow[2][i], self.blue[2-i][2] = self.blue[2-i][2], self.white[0][2-i], self.green[i][0], self.yellow[2][i]
            
        elif side == 'blue':
            self.blue = [list(r) for r in zip(*self.blue[::-1])]
            # w -> o -> y -> r
            for i in range(3):
                self.white[i][2], self.orange[2-i][0], self.yellow[i][2], self.red[i][2] = self.red[i][2], self.white[i][2], self.orange[2-i][0], self.yellow[i][2]
            
        elif side == 'green':
            self.green = [list(r) for r in zip(*self.green[::-1])]
            # w -> r -> y -> o
            for i in range(3):
                self.white[i][0], self.red[i][0], self.yellow[i][0], self.orange[2-i][2] = self.orange[2-i][2], self.white[i][0], self.red[i][0], self.yellow[i][0]

    def turn_side_anti_clockwise(self, side):
        """Turn side in the anticlockwise direction"""
        if side == 'white':
            self.white = [list(r) for r in zip(*self.white)][::-1]
            # b -> o -> g -> r
            self.blue[0], self.red[0], self.green[0], self.orange[0] = self.red[0], self.green[0], self.orange[0], self.blue[0]
            
        elif side == 'yellow':
            self.yellow = [list(r) for r in zip(*self.yellow)][::-1]
            # b -> r -> g -> o
            self.blue[2], self.red[2], self.green[2], self.orange[2] = self.orange[2], self.blue[2], self.red[2], self.green[2]
            
        elif side == 'red':
            self.red = [list(r) for r in zip(*self.red)][::-1]
            # w -> g -> y -> b
            for i in range(3):
                self.white[2][i], self.blue[i][0], self.yellow[0][2-i], self.green[2-i][2] = self.blue[i][0], self.yellow[0][2-i], self.green[2-i][2], self.white[2][i]
            
        elif side == 'orange':
            self.orange = [list(r) for r in zip(*self.orange)][::-1]
            # w -> b -> y -> g
            for i in range(3):
                self.white[0][2-i], self.green[i][0], self.yellow[2][i], self.blue[2-i][2] = self.green[i][0], self.yellow[2][i], self.blue[2-i][2], self.white[0][2-i]
            
        elif side == 'blue':
            self.blue = [list(r) for r in zip(*self.blue)][::-1]
            # w -> r -> y -> o
            for i in range(3):
                self.white[i][2], self.orange[2-i][0], self.yellow[i][2], self.red[i][2] = self.orange[2-i][0], self.yellow[i][2], self.red[i][2], self.white[i][2]
            
        elif side == 'green':
            self.green = [list(r) for r in zip(*self.green)][::-1]
            # w -> o -> y -> r
            for i in range(3):
                self.white[i][0], self.red[i][0], self.yellow[i][0], self.orange[2-i][2] = self.red[i][0], self.yellow[i][0], self.orange[2-i][2], self.white[i][0]

    def check_if_solved(self):
        """Check if the cube is in a solved state"""
        for x in range(0,3):
            for y in range (0,3):
                if (
                        self.white[x][y] != 'w' or
                        self.yellow[x][y] != 'y' or
                        self.red[x][y] != 'r' or
                        self.orange[x][y] != 'o' or
                        self.blue[x][y] != 'b' or
                        self.green[x][y] != 'g'
                        ):
                    return False
        return True

    def scramble(self):
        """Randomise the cube"""
        colours = ['white', 'white', 'yellow', 'yellow', 'red', 'red',
                   'orange', 'orange', 'blue', 'blue', 'green', 'green']
        for _ in range(random.randint(80,120)):
            x = random.randint(0,11) # Even moves clockwise odd moves anti           
            if x % 2 == 0:
                self.turn_side_clockwise(colours[x])
            else:
                self.turn_side_anti_clockwise(colours[x])
