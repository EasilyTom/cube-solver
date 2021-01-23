from cube import RubiksCube
from os import mkdir
import random
import csv

def _range(x=1, y=1, z=1):
    for _x in range(x):
        for _y in range(y):
            for _z in range(z):
                yield _x, _y, _z


    
class TestCase:
    def __init__(self, complexity):
        self.cubearr = RubiksCube()
        self.truemoves = ''

        for _ in range(complexity):
            COLOURS = ['white', 'white', 'yellow', 'yellow', 'red', 'red',
                       'orange', 'orange', 'blue', 'blue', 'green', 'green']
            x = random.randint(0, 11)
            if x % 2 == 0:
                self.cubearr.turn_side_clockwise(COLOURS[x])
                self.truemoves += COLOURS[x][0].upper()
            else:
                self.cubearr.turn_side_anti_clockwise(COLOURS[x])
                self.truemoves += COLOURS[x][0].lower()

    def get_moves(self):
        return self.truemoves[::-1]

    def get_arr(self):
        return self.cubearr

    def get_data(self):
        """Returns touple of 2D arrays ordered WYROBG"""
        sides = (self.cubearr.white, self.cubearr.yellow, self.cubearr.red,
                self.cubearr.orange, self.cubearr.blue, self.cubearr.green)
        data = ''
        for x, y, z in _range(6, 3, 3):
            data += sides[x][y][z]
        return data


# ID, TrueMoves, White, Yellow, Red, Orange, Blue, Green
def create_data():
    NUM_OF_ENTRIES = 10000

    try:
        print('Attempting to make data folder')
        mkdir('data')
        print('Folder created successfully')
    except FileExistsError:
        print('Folder already exists')

    def create_row(num, complexity):
        case = TestCase(complexity)
        moves = case.get_moves()
        sides = case.get_data()
        data = [num, moves, sides]
        name = ('data/test_data_' + str(complexity) + '.csv')
        with open(name, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    for com in range(1, 21):
        print('Creating file', com)
        for x in range(NUM_OF_ENTRIES):
            if (x / (NUM_OF_ENTRIES/100))%5 == 0:
                print(str(int(x / (NUM_OF_ENTRIES/100))) + '%')
            create_row(x, com)

create_data()
