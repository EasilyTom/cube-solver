from Cube import RubiksCube
import simpleai

cube = RubiksCube
cube.scramble()

# Semi- solved states
# first stage is white edges around yellow centre
daisy = [['e', 'w', 'e'],
         ['w', 'y', 'w'],
         ['e', 'w', 'e']]

