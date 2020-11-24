from solver import solve
import cube
import gui

cube_model = gui.model
cube_array = cube.RubiksCube(cube_model)

cube_array.turn_side_clockwise('white')
cube_array.turn_side_clockwise('red')
