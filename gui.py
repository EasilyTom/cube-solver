import vpython as vpy
from time import sleep    
                
        
def _range_2d(xrange, yrange):
    for x in range(xrange):
        for y in range(yrange):
            yield x, y

class side:
    def __init__(self, side):
        
        self.side = side
        self.locations = []
        if self.side == 'white':
            for x, z in _range_2d(3, 3):
                self.locations.append((x, 2, z))
        elif self.side == 'yellow':
            for x, z in _range_2d(3, 3):
                self.locations.append((x, 0, z))
        elif self.side == 'red': 
            for y, z in _range_2d(3, 3):
                self.locations.append((0, y, z))
        elif self.side == 'orange':
            for y, z in _range_2d(3, 3):
                self.locations.append((2, y, z))
        elif self.side == 'blue':
            for x, y in _range_2d(3, 3):
                self.locations.append((x, y, 2))
        elif self.side == 'green':
            for x, y in _range_2d(3, 3):
                self.locations.append((x, y, 0))
        else:
            raise Exception('Invalid Side')
            

    def get_side(self, cube):
        self.colours = []
        for x, y, z in self.locations:
            self.colours.append(cube[x][y][z])
        self.colours = [self.colours[0:3],
                        self.colours[3:6],
                        self.colours[6:9]]
        return self.colours
        
    def rotate_side(self, cube, prime):
        self.oneD = []
        self.colours = self.get_side(cube)
        
        if prime:
            self.colours =  [list(r) for r in zip(*self.colours[::-1])]
        else:
            self.colours =  [list(r) for r in zip(*self.colours)][::-1]
            
        for x, y in _range_2d(3, 3):
            self.oneD.append(self.colours[x][y])
        
        i = 0 # Bad practice need to fix later
        for x, y, z in self.locations:
            cube[x][y][z] = self.oneD[i]
            i += 1
        return cube
            
class model:
                
    def __init__(self):
        
        self.LOOP_FRAMES = 500
        self.MOVE_TIME = 0.1
                    
        def create_cubelet(a, b, c):
            a = a * 1.05  # To give a 0.05 gap between each cubelet
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
        
        

        self.cube_model = ([[[create_cubelet(x, y, z) for z in range(3)]
                           for y in range(3)] for x in range(3)])
        
        
        self.white = side('white')
        self.yellow = side('yellow')
        self.red = side('red')
        self.orange = side('orange')
        self.blue = side('blue')
        self.green = side('green')
    
    def _range_3d(self, xrange, yrange, zrange):                
        for x in range(xrange):
            for y in range(yrange):
                for z in range(zrange):
                    yield x, y, z
    
    
    def turn_white(self, prime=False):
        if prime:
            direction = 90
        else:
            direction = -90
            
        for _ in range(self.LOOP_FRAMES):
            for x, z in _range_2d(3, 3):
                active = self.cube_model[x][2][z]
                active.rotate(angle=vpy.radians(direction/self.LOOP_FRAMES),
                              axis=vpy.vector(0,1,0),
                              origin=vpy.vector(1.05,1.55,1.55))
            sleep(self.MOVE_TIME/self.LOOP_FRAMES)
            
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
            sleep(self.MOVE_TIME/self.LOOP_FRAMES)

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
            sleep(self.MOVE_TIME/self.LOOP_FRAMES)

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
            sleep(self.MOVE_TIME/self.LOOP_FRAMES)

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
            sleep(self.MOVE_TIME/self.LOOP_FRAMES)

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
            sleep(self.MOVE_TIME/self.LOOP_FRAMES)

        self.cube_model = self.yellow.rotate_side(self.cube_model, prime)


if __name__ == '__main__':
    model = model()
    model.turn_white()
    model.turn_red()
