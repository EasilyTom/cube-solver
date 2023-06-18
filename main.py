import vpython as vpy
import random

from HumanSolver.cube import RubiksCube as HumanCube
from HumanSolver.solver import solve as HumanSolve

from PDBsolver.common import parse as PDBparse
from PDBsolver.common import CUBE_INIT
from PDBsolver.ida import Astar as PDBsolve

def _range_2d(xrange, yrange):
    '''Simple 2D generator'''
    for x in range(xrange):
        for y in range(yrange):
            yield x, y

class model:

    def __init__(self):

        def create_cubelet(a, b, c):
            '''Returns a cubelet object, constructed of pyramids'''
            a = a * 1.05 # To give a 0.05 gap between each cubelet
            b = b * 1.05
            c = c * 1.05

            cubelet = [vpy.pyramid(pos=vpy.vector(a,b,c), 
                                   axis=vpy.vector(0,0,1),
                                   color=vpy.color.green),

                        vpy.pyramid(pos=vpy.vector(a,b,c+1),
                                    axis=vpy.vector(0,0,-1),
                                    color=vpy.color.blue),
                        
                       vpy.pyramid(pos=vpy.vector(a-0.5,b,c+0.5),
                                   axis=vpy.vector(1,0,0),
                                   color=vpy.color.red),
                        
                       vpy.pyramid(pos=vpy.vector(a+0.5,b,c+0.5),
                                   axis=vpy.vector(-1,0,0),
                                   color=vpy.color.orange),
                        
                       vpy.pyramid(pos=vpy.vector(a,b+0.5,c+0.5),
                                   axis=vpy.vector(0,-1,0),
                                    color=vpy.color.white),
                        
                       vpy.pyramid(pos=vpy.vector(a,b-0.5,c+0.5),
                                   axis=vpy.vector(0,1,0),
                                   color=vpy.color.yellow)
                       ]
            return vpy.compound(cubelet)


        class side:
            '''Subclass used to hold the cubelets associated with each side of the cube'''
            def __init__(self, side):

                self.side = side
                self.locations = []
                self.boy = True # For some reason the b, o, y sides have to be rotated the opposite direction
                if self.side == 'white':
                    for x, z in _range_2d(3, 3):
                        self.locations.append((x, 2, z))
                        self.boy = False
                elif self.side == 'yellow':
                    for x, z in _range_2d(3, 3):
                        self.locations.append((x, 0, z))
                elif self.side == 'red': 
                    for y, z in _range_2d(3, 3):
                        self.locations.append((0, y, z))
                        self.boy = False
                elif self.side == 'orange':
                    for y, z in _range_2d(3, 3):
                        self.locations.append((2, y, z))
                elif self.side == 'blue':
                    for x, y in _range_2d(3, 3):
                        self.locations.append((x, y, 2))
                elif self.side == 'green':
                    for x, y in _range_2d(3, 3):
                        self.locations.append((x, y, 0))
                        self.boy = False
                else:
                    raise Exception('Invalid Side')


            def get_side(self, cube):
                colours = []
                for x, y, z in self.locations:
                    colours.append(cube[x][y][z])
                colours = [colours[0:3],
                           colours[3:6],
                           colours[6:9]]
                return colours

            def rotate_side(self, cube, prime):
                oneD = []
                colours = self.get_side(cube)
                if self.boy: prime = not prime

                if prime:
                    colours =  [list(r) for r in zip(*colours[::-1])]
                else:
                    colours =  [list(r) for r in zip(*colours)][::-1]

                for x, y in _range_2d(3, 3):
                    oneD.append(colours[x][y])

                for i, x in enumerate(self.locations):
                    cube[x[0]][x[1]][x[2]] = oneD[i]
                return cube

        # Create the cubelet objects, stored in a 3D array
        self.cube_model = ([[[create_cubelet(x, y, z) for z in range(3)]
                           for y in range(3)] for x in range(3)])
        
        # How many frames to use for each quarter turn
        self.LOOP_FRAMES = 5
        # How long to sleep after each frame
        self.SPF = 0.001/self.LOOP_FRAMES
        
        self.white = side('white')
        self.yellow = side('yellow')
        self.red = side('red')
        self.orange = side('orange')
        self.blue = side('blue')
        self.green = side('green')
    
    def turn_white(self, prime=False):
        if prime:
            direction = 90
        else:
            direction = -90
            
        ANGLE = vpy.radians(direction/self.LOOP_FRAMES) # How far to turn each frame. 
        AXIS = vpy.vector(0,1,0) # The direction to turn.
        ORIGIN = vpy.vector(1.05,1.55,1.55) # The point to rotate about
        
        for _ in range(self.LOOP_FRAMES):
            for x, z in _range_2d(3, 3): # Move each of the 9 cubelets.
                active = self.cube_model[x][2][z]
                active.rotate(angle=ANGLE,
                              axis=AXIS,
                              origin=ORIGIN)
            vpy.sleep(self.SPF) # Slows down the turn. vpy.sleep vs time.sleep allows the rest of the gui to keep working

        self.cube_model = self.white.rotate_side(self.cube_model, prime)
        
    def turn_red(self, prime=False):
        if prime:
            direction = -90
        else:
            direction = 90
            
        for _ in range(self.LOOP_FRAMES):
            for y, z in _range_2d(3, 3):
                active = self.cube_model[0][y][z]
                active.rotate(angle=vpy.radians(direction/self.LOOP_FRAMES),
                              axis=vpy.vector(1,0,0),
                              origin=vpy.vector(-0.5,1.05,1.55))
            vpy.sleep(self.SPF)

        self.cube_model = self.red.rotate_side(self.cube_model, prime)
            
    def turn_blue(self, prime=False):
        if prime:
            direction = 90
        else:
            direction = -90
            
        for _ in range(self.LOOP_FRAMES):
            for x, y in _range_2d(3, 3):
                active = self.cube_model[x][y][2]
                active.rotate(angle=vpy.radians(direction/self.LOOP_FRAMES),
                              axis=vpy.vector(0,0,1),
                              origin=vpy.vector(1.05,1.05,1.05))
            vpy.sleep(self.SPF)

        self.cube_model = self.blue.rotate_side(self.cube_model, prime)
        
    def turn_orange(self, prime=False):
        if prime:
            direction = 90
        else:
            direction = -90
            
        for _ in range(self.LOOP_FRAMES):
            for y, z in _range_2d(3, 3):
                active = self.cube_model[2][y][z]
                active.rotate(angle=vpy.radians(direction/self.LOOP_FRAMES),
                              axis=vpy.vector(1,0,0),
                              origin=vpy.vector(-0.5,1.05,1.55))
            vpy.sleep(self.SPF)

        self.cube_model = self.orange.rotate_side(self.cube_model, prime)

    def turn_green(self, prime=False):
        if prime:
            direction = -90
        else:
            direction = 90
            
        for _ in range(self.LOOP_FRAMES):
            for x, y in _range_2d(3, 3):
                active = self.cube_model[x][y][0]
                active.rotate(angle=vpy.radians(direction/self.LOOP_FRAMES),
                              axis=vpy.vector(0,0,1),
                              origin=vpy.vector(1.05,1.05,1.05))
            vpy.sleep(self.SPF)

        self.cube_model = self.green.rotate_side(self.cube_model, prime)

    def turn_yellow(self, prime=False):
        if prime:
            direction = -90
        else:
            direction = 90
            
        for _ in range(self.LOOP_FRAMES):
            for x, z in _range_2d(3, 3):
                active = self.cube_model[x][0][z]
                active.rotate(angle=vpy.radians(direction/self.LOOP_FRAMES),
                              axis=vpy.vector(0,1,0),
                              origin=vpy.vector(1.05,1.55,1.55))
            vpy.sleep(self.SPF)

        self.cube_model = self.yellow.rotate_side(self.cube_model, prime)

    def parse(self, st):
        '''Parse a series of moves.
           Uppercase is clockwise, Lowercase is anti.
'''
        MOVES = {'w': self.turn_white,
                 'y': self.turn_yellow,
                 'r': self.turn_red,
                 'o': self.turn_orange,
                 'b': self.turn_blue,
                 'g': self.turn_green}
        for m in st:
            MOVES[m.lower()](m.islower())

    def quickparse(self, st):
        MOVES = {'w': self.turn_white,
                 'y': self.turn_yellow,
                 'r': self.turn_red,
                 'o': self.turn_orange,
                 'b': self.turn_blue,
                 'g': self.turn_green}
        delay = self.SPF
        self.SPF = 0

        for m in st:
            MOVES[m.lower()](m.islower())
            vpy.sleep(.1)
        self.SPF = delay


class UI():
    def __init__(self):
        # Initiate data structures
        self.model = model()
        self.human_cube = HumanCube()
        self.PDBcube = CUBE_INIT

        def redir(b):
            # Allows the buttons to pass arguments to the execute method
            self.execute(b.st)
        # Movement buttons
        self.W = vpy.button(bind=redir, text = '↷', background=vpy.color.white, st='W')
        self.w = vpy.button(bind=redir, text = '↶', background=vpy.color.white, st='w')
        self.Y = vpy.button(bind=redir, text = '↷', background=vpy.color.yellow, st='Y')
        self.y = vpy.button(bind=redir, text = '↶', background=vpy.color.yellow, st='y')
        self.R = vpy.button(bind=redir, text = '↷', background=vpy.color.red, st='R')
        self.r = vpy.button(bind=redir, text = '↶', background=vpy.color.red, st='r')
        self.O = vpy.button(bind=redir, text = '↷', background=vpy.color.orange, st='O')
        self.o = vpy.button(bind=redir, text = '↶', background=vpy.color.orange, st='o')
        self.B = vpy.button(bind=redir, text = '↷', background=vpy.color.blue, st='B')
        self.b = vpy.button(bind=redir, text = '↶', background=vpy.color.blue, st='b')
        self.G = vpy.button(bind=redir, text = '↷', background=vpy.color.green, st='G')
        self.g = vpy.button(bind=redir, text = '↶', background=vpy.color.green, st='g')

        # Solver Menu
        def autosolve(b):
            if b.selected == 'Human':
                ml = HumanSolve(self.human_cube)
                self.quickexecute(ml)
            elif b.selected == 'PDB':
                ml = PDBsolve(self.PDBcube)
                if ml == -1:
                    print('Cube not solvable')
                else:
                    self.quickexecute(ml)
            b.selected = 'Solvers'
        self.autosolve = vpy.menu(choices=['Solvers', 'Human', 'PDB'], bind=autosolve)

        # Scramble button
        def scramble(b):
            """Randomise the cube"""
            COLOURS = ['w', 'W', 'y', 'Y', 'r', 'R',
                       'o', 'O', 'b', 'B', 'g', 'G']
            for _ in range(random.randint(40,60)):
                x = random.randint(0,11)            
                self.quickexecute(COLOURS[x])

        self.scramble = vpy.button(bind=scramble, text='Scramble')

        # Reset button
        def reset(b):
            for x in self.model.cube_model:
                for y in x:
                    for i in y:
                        i.visible = False # It isn't possible to delete the cube.
            del self.model                # So hide it and make a new one
            self.model = model()
            self.human_cube = HumanCube()
            self.PDBcube = CUBE_INIT

        self.reset = vpy.button(bind=reset, text='Reset')


    # Execute a series of moves
    def execute(self, st):
        self.model.parse(st)
        self.human_cube.parse(st)
        PDBparse(self.PDBcube, st)

    # Execute a series of moves *quickly*
    def quickexecute(self, st):
        self.model.quickparse(st)
        print(st)
        self.human_cube.parse(st)
        PDBparse(self.PDBcube, st)

if __name__ == '__main__':
    scene=vpy.canvas(center=vpy.vector(1.05, 1.05, 1.575))
    ui = UI()
