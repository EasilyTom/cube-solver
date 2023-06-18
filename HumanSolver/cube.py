import random


class RubiksCube:

    def __init__(self):

        self.move_list = ''
        
            # Creates  2D arrays for each side
            #  W
            # GRBO
            #  Y
                           #o
        self.white = [['w','w','w'],
                      ['w','w','w'],
                      ['w','w','w']]

                         #w
        self.red = [['r','r','r'],
                    ['r','r','r'],
                    ['r','r','r']]

                            #w
        self.orange = [['o','o','o'],
                       ['o','o','o'],
                       ['o','o','o']]
        
                           #w
        self.green = [['g','g','g'],
                      ['g','g','g'],
                      ['g','g','g']]
        
                          #w
        self.blue = [['b','b','b'],
                     ['b','b','b'],
                     ['b','b','b']]

                            #r
        self.yellow = [['y','y','y'],
                       ['y','y','y'],
                       ['y','y','y']]


    def turn_side(self, side):
        """Turn a side. Uppercase is clockwise, lower is anticlockwise"""
        # Sorry PEP8
        # The long lines of code move the edges of the face around
        if side == 'W':
            self.white = [list(r) for r in zip(*self.white[::-1])]
            # b -> r -> g -> o
            self.blue[0], self.red[0], self.green[0], self.orange[0] = self.orange[0], self.blue[0], self.red[0], self.green[0]

        elif side == 'Y':
            self.yellow = [list(r) for r in zip(*self.yellow[::-1])]
            # b-> o -> g -> r
            self.blue[2], self.red[2], self.green[2], self.orange[2] = self.red[2], self.green[2], self.orange[2], self.blue[2]
            
        elif side == 'R':
            self.red = [list(r) for r in zip(*self.red[::-1])]
            # w -> b -> y -> g
            for i in range(3):
                self.white[2][i], self.blue[i][0], self.yellow[0][2-i], self.green[2-i][2] = self.green[2-i][2], self.white[2][i], self.blue[i][0], self.yellow[0][2-i]
            
        elif side == 'O':
            self.orange = [list(r) for r in zip(*self.orange[::-1])]
            # w -> g -> y -> b
            for i in range(3):
                self.white[0][2-i], self.green[i][0], self.yellow[2][i], self.blue[2-i][2] = self.blue[2-i][2], self.white[0][2-i], self.green[i][0], self.yellow[2][i]
            
        elif side == 'B':
            self.blue = [list(r) for r in zip(*self.blue[::-1])]
            # w -> o -> y -> r
            for i in range(3):
                self.white[i][2], self.orange[2-i][0], self.yellow[i][2], self.red[i][2] = self.red[i][2], self.white[i][2], self.orange[2-i][0], self.yellow[i][2]
            
        elif side == 'G':
            self.green = [list(r) for r in zip(*self.green[::-1])]
            # w -> r -> y -> o
            for i in range(3):
                self.white[i][0], self.red[i][0], self.yellow[i][0], self.orange[2-i][2] = self.orange[2-i][2], self.white[i][0], self.red[i][0], self.yellow[i][0]
    
        elif side == 'w':
            self.white = [list(r) for r in zip(*self.white)][::-1]
            # b -> o -> g -> r
            self.blue[0], self.red[0], self.green[0], self.orange[0] = self.red[0], self.green[0], self.orange[0], self.blue[0]
            
        elif side == 'y':
            self.yellow = [list(r) for r in zip(*self.yellow)][::-1]
            # b -> r -> g -> o
            self.blue[2], self.red[2], self.green[2], self.orange[2] = self.orange[2], self.blue[2], self.red[2], self.green[2]
            
        elif side == 'r':
            self.red = [list(r) for r in zip(*self.red)][::-1]
            # w -> g -> y -> b
            for i in range(3):
                self.white[2][i], self.blue[i][0], self.yellow[0][2-i], self.green[2-i][2] = self.blue[i][0], self.yellow[0][2-i], self.green[2-i][2], self.white[2][i]
            
        elif side == 'o':
            self.orange = [list(r) for r in zip(*self.orange)][::-1]
            # w -> b -> y -> g
            for i in range(3):
                self.white[0][2-i], self.green[i][0], self.yellow[2][i], self.blue[2-i][2] = self.green[i][0], self.yellow[2][i], self.blue[2-i][2], self.white[0][2-i]
            
        elif side == 'b':
            self.blue = [list(r) for r in zip(*self.blue)][::-1]
            # w -> r -> y -> o
            for i in range(3):
                self.white[i][2], self.orange[2-i][0], self.yellow[i][2], self.red[i][2] = self.orange[2-i][0], self.yellow[i][2], self.red[i][2], self.white[i][2]
            
        elif side == 'g':
            self.green = [list(r) for r in zip(*self.green)][::-1]
            # w -> o -> y -> r
            for i in range(3):
                self.white[i][0], self.red[i][0], self.yellow[i][0], self.orange[2-i][2] = self.red[i][0], self.yellow[i][0], self.orange[2-i][2], self.white[i][0]
        else:
            raise Exception('Invalid Side')
        self.move_list += side

    def parse(self, string):
        '''Execute a series of moves

            Uppercase is clockwise, Lowercase is anticlockwise
'''
        for i in string:
            self.turn_side(i)
        
        
    def is_solved(self):
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
        """Randomise the cube. Returns the list of moves performed"""
        COLOURS = ['w', 'W', 'y', 'Y', 'r', 'R',
                   'o', 'O', 'b', 'B', 'g', 'G']
        li = ''
        for _ in range(random.randint(40,60)):
            x = random.randint(0,11)            
            self.turn_side(COLOURS[x])
            li += COLOURS[x]
        return li
            

    def out_sides(self):
        '''Debugging. Output all the faces'''
        print('white: ' + str(self.white)
              +'\nyellow: ' + str(self.yellow)
              +'\nred: ' + str(self.red)
              +'\norange: ' + str(self.orange)
              +'\nblue: ' + str(self.blue)
              +'\ngreen: ' + str(self.green)
              )
        
    def reset_moves(self):
        '''Reset the list of previous moves. Does not reset the cube itself'''
        self.move_list = ''

if __name__ == '__main__':
    #tests
    arr = RubiksCube()
    arr.out_sides()
    arr.parse('w')
    arr.out_sides()
