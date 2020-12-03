import vpython as vpy
from time import sleep    


def cubelet(a, b, c):
    if a == 1:
        a = 1.05
    elif a == 2:
        a = 2.1

    if b == 1:
        b = 1.05
    elif b == 2:
        b = 2.1

    if c == 1:
        c = 1.05
    elif c == 2:
        c = 2.1
        
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

        
class model:
    
    LOOP_FRAMES = 1000
    MOVE_TIME = 0.1

    cube_model = [[[None, None, None],
                   [None, None, None],
                   [None, None, None]],

                  [[None, None, None],
                  [None, None, None],
                  [None, None, None]],

                  [[None, None, None],
                  [None, None, None],
                  [None, None, None]]]
    

    for x in range(3):
        for y in range(3):
            for z in range(3):
                cube_model[x][y][z] = cubelet(x, y, z)
    
    def turn_white(prime):
        if prime:
            direction = 90
        else:
            direction = -90
            
        for _ in range(model.LOOP_FRAMES):
            for x in range(3):
                for z in range(3):
                    active = model.cube_model[x][2][z]
                    active.rotate(angle=vpy.radians(direction/model.LOOP_FRAMES),
                                  axis=vpy.vector(0,1,0),
                                  origin=vpy.vector(1.05,1.55,1.55))
            sleep(model.MOVE_TIME/model.LOOP_FRAMES)

        temp = []
        for i in range(3):
                temp.append(model.cube_model[i][2])
        model.cube_model = [list(r) for r in zip(*self.yellow[::-1])]
        print(temp)
        
    def turn_red(prime):
        if prime:
            direction = -90
        else:
            direction = 90
            
        for _ in range(model.LOOP_FRAMES):
            for y in range(3):
                for z in range(3):
                    active = model.cube_model[0][y][z]
                    active.rotate(angle=vpy.radians(direction/model.LOOP_FRAMES),
                                  axis=vpy.vector(1,0,0),
                                  origin=vpy.vector(-0.5,1.05,1.55))
            sleep(model.MOVE_TIME/model.LOOP_FRAMES)
            

    def turn_blue(prime):
        if prime:
            direction = 90
        else:
            direction = -90
            
        for _ in range(model.LOOP_FRAMES):
            for x in range(3):
                for y in range(3):
                    active = model.cube_model[x][y][2]
                    active.rotate(angle=vpy.radians(direction/model.LOOP_FRAMES),
                                  axis=vpy.vector(0,0,1),
                                  origin=vpy.vector(1.05,1.05,1.05))
            sleep(model.MOVE_TIME/model.LOOP_FRAMES)

    def turn_orange(prime):
        if prime:
            direction = 90
        else:
            direction = -90
            
        for _ in range(model.LOOP_FRAMES):
            for y in range(3):
                for z in range(3):
                    active = model.cube_model[2][y][z]
                    active.rotate(angle=vpy.radians(direction/model.LOOP_FRAMES),
                                  axis=vpy.vector(1,0,0),
                                  origin=vpy.vector(-0.5,1.05,1.55))
            sleep(model.MOVE_TIME/model.LOOP_FRAMES)

    def turn_green(prime):
        if prime:
            direction = -90
        else:
            direction = 90
            
        for _ in range(model.LOOP_FRAMES):
            for x in range(3):
                for y in range(3):
                    active = model.cube_model[x][y][0]
                    active.rotate(angle=vpy.radians(direction/model.LOOP_FRAMES),
                                  axis=vpy.vector(0,0,1),
                                  origin=vpy.vector(1.05,1.05,1.05))
            sleep(model.MOVE_TIME/model.LOOP_FRAMES)

    def turn_yellow(prime):
        if prime:
            direction = -90
        else:
            direction = 90
            
        for _ in range(model.LOOP_FRAMES):
            for x in range(3):
                for z in range(3):
                    active = model.cube_model[x][0][z]
                    active.rotate(angle=vpy.radians(direction/model.LOOP_FRAMES),
                                  axis=vpy.vector(0,1,0),
                                  origin=vpy.vector(1.05,1.55,1.55))
            sleep(model.MOVE_TIME/model.LOOP_FRAMES)
