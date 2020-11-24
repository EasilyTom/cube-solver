from gui import model
import random


class RubiksCube:

    def __init__(self, model):
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
            model.turn_white(False)
            self.white = [list(r) for r in zip(*self.white[::-1])]
            # b -> r -> g -> o
            self.blue[0], self.red[0], self.green[0], self.orange[0] = self.orange[0], self.blue[0], self.red[0], self.green[0]

        elif side == 'yellow':
            model.turn_yellow(False)
            self.yellow = [list(r) for r in zip(*self.yellow[::-1])]
            # b-> o -> g -> r
            self.blue[2], self.red[2], self.green[2], self.orange[2] = self.red[2], self.green[2], self.orange[2], self.blue[2]
            
        elif side == 'red':
            model.turn_red(False)
            self.red = [list(r) for r in zip(*self.red[::-1])]
            # w -> b -> y -> g
            self.white[2][0], self.blue[0][0], self.yellow[0][2], self.green[2][2] = self.green[2][2], self.white[2][0], self.blue[0][0], self.yellow[0][2]
            self.white[2][1], self.blue[1][0], self.yellow[0][1], self.green[1][2] = self.green[1][2], self.white[2][1], self.blue[1][0], self.yellow[0][1]
            self.white[2][2], self.blue[2][0], self.yellow[0][0], self.green[0][2] = self.green[0][2], self.white[2][2], self.blue[2][0], self.yellow[0][0]
            
        elif side == 'orange':
            model.turn_orange(False)
            self.orange = [list(r) for r in zip(*self.orange[::-1])]
            # w -> g -> y -> b
            self.white[0][2], self.green[0][0], self.yellow[2][0], self.blue[2][2] = self.blue[2][2], self.white[0][2], self.green[0][0], self.yellow[2][0]
            self.white[0][1], self.green[1][0], self.yellow[2][1], self.blue[1][2] = self.blue[1][2], self.white[0][1], self.green[1][0], self.yellow[2][1]
            self.white[0][0], self.green[2][0], self.yellow[2][2], self.blue[0][2] = self.blue[0][2], self.white[0][0], self.green[2][0], self.yellow[2][2]
            
        elif side == 'blue':
            model.turn_blue(False)
            self.blue = [list(r) for r in zip(*self.blue[::-1])]
            # w -> o -> y -> r
            self.white[0][2], self.orange[2][0], self.yellow[0][2], self.red[0][2] = self.red[0][2], self.white[0][2], self.orange[2][0], self.yellow[0][2]
            self.white[1][2], self.orange[1][0], self.yellow[1][2], self.red[1][2] = self.red[1][2], self.white[1][2], self.orange[1][0], self.yellow[1][2]
            self.white[2][2], self.orange[0][0], self.yellow[2][2], self.red[2][2] = self.red[2][2], self.white[2][2], self.orange[0][0], self.yellow[2][2]
            
        elif side == 'green':
            model.turn_green(False)
            self.green = [list(r) for r in zip(*self.green[::-1])]
            # w -> r -> y -> o
            self.white[0][0], self.red[0][0], self.yellow[0][0], self.orange[2][2] = self.orange[2][2], self.white[0][0], self.red[0][0], self.yellow[0][0]
            self.white[1][0], self.red[1][0], self.yellow[1][0], self.orange[1][2] = self.orange[1][2], self.white[1][0], self.red[1][0], self.yellow[1][0]
            self.white[2][0], self.red[2][0], self.yellow[2][0], self.orange[0][2] = self.orange[0][2], self.white[2][0], self.red[2][0], self.yellow[2][0]

    def turn_side_anti_clockwise(self, side):
        """Turn side in the anticlockwise direction"""
        if side == 'white':
            model.turn_white(True)
            self.white = [list(r) for r in zip(*self.white)][::-1]
            # b -> o -> g -> r
            self.blue[0], self.red[0], self.green[0], self.orange[0] = self.red[0], self.green[0], self.orange[0], self.blue[0]
            
        elif side == 'yellow':
            model.turn_yellow(True)
            self.yellow = [list(r) for r in zip(*self.yellow)][::-1]
            # b -> r -> g -> o
            self.blue[2], self.red[2], self.green[2], self.orange[2] = self.orange[2], self.blue[2], self.red[2], self.green[2]
            
        elif side == 'red':
            model.turn_red(True)
            self.red = [list(r) for r in zip(*self.red)][::-1]
            # w -> g -> y -> b
            self.white[2][0], self.blue[0][0], self.yellow[0][2], self.green[2][2] = self.blue[0][0], self.yellow[0][2], self.green[2][2], self.white[2][0]
            self.white[2][1], self.blue[1][0], self.yellow[0][1], self.green[1][2] = self.blue[1][0], self.yellow[0][1], self.green[1][2], self.white[2][1]
            self.white[2][2], self.blue[2][0], self.yellow[0][0], self.green[0][2] = self.blue[2][0], self.yellow[0][0], self.green[0][2], self.white[2][2]
            
        elif side == 'orange':
            model.turn_orange(True)
            self.orange = [list(r) for r in zip(*self.orange)][::-1]
            # w -> b -> y -> g
            self.white[0][2], self.green[0][0], self.yellow[2][0], self.blue[2][2] = self.green[0][0], self.yellow[2][0], self.blue[2][2], self.white[0][2]
            self.white[0][1], self.green[1][0], self.yellow[2][1], self.blue[1][2] = self.green[1][0], self.yellow[2][1], self.blue[1][2], self.white[0][1] 
            self.white[0][0], self.green[2][0], self.yellow[2][2], self.blue[0][2] = self.green[2][0], self.yellow[2][2], self.blue[0][2], self.white[0][0]
            
        elif side == 'blue':
            model.turn_blue(True)
            self.blue = [list(r) for r in zip(*self.blue)][::-1]
            # w -> r -> y -> o
            self.white[0][2], self.orange[2][0], self.yellow[0][2], self.red[0][2] = self.orange[2][0], self.yellow[0][2], self.red[0][2], self.white[0][2]
            self.white[1][2], self.orange[1][0], self.yellow[1][2], self.red[1][2] = self.orange[1][0], self.yellow[1][2], self.red[1][2], self.white[1][2]
            self.white[2][2], self.orange[0][0], self.yellow[2][2], self.red[2][2] = self.orange[0][0], self.yellow[2][2], self.red[2][2], self.white[2][2]
            
        elif side == 'green':
            model.turn_green(True)
            self.green = [list(r) for r in zip(*self.green)][::-1]
            # w -> o -> y -> r
            self.white[0][0], self.red[0][0], self.yellow[0][0], self.orange[2][2] = self.red[0][0], self.yellow[0][0], self.orange[2][2], self.white[0][0]
            self.white[1][0], self.red[1][0], self.yellow[1][0], self.orange[1][2] = self.red[1][0], self.yellow[1][0], self.orange[1][2], self.white[1][0]
            self.white[2][0], self.red[2][0], self.yellow[2][0], self.orange[0][2] = self.red[2][0], self.yellow[2][0], self.orange[0][2], self.white[2][0]

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
