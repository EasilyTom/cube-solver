from solver import solve
import cube
import gui
import time
cube_model = gui.model()
cube_array = cube.RubiksCube()

#scramlist = cube_array.scramble()

#cube_model.parse(scramlist)
cube_model.parse('W')
