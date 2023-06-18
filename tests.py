#Human and PDB tests

import unittest
import copy
import random


import PDBsolver.common as common
import PDBsolver.hasher as hasher
import PDBsolver.ida as ida

from HumanSolver.cube import RubiksCube
import HumanSolver.solver as solver

def CUBE_INIT():
    '''Prevents tests altering the global and incuring side effects'''
    return copy.deepcopy(common.CUBE_INIT)

class TestCommon(unittest.TestCase):
    def test_solved(self):
        self.assertTrue(common.isSolved(common.CUBE_INIT))

    def test_parse_wc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'W')
        self.assertEqual(arr, [[[3, 0], [0, 0], [1, 0], [2, 0], [4, 1], [5, 1], [6, 1], [7, 1]],
                               [[1, 0], [2, 0], [3, 0], [0, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]], 'W'])

    def test_parse_wcc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'w')
        self.assertEqual(arr, [[[1, 0], [2, 0], [3, 0], [0, 0], [4, 1], [5, 1], [6, 1], [7, 1]],
                               [[3, 0], [0, 0], [1, 0], [2, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0]], 'w'])

    def test_parse_yc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'Y')
        self.assertEqual(arr, [[[0, 0], [1, 0], [2, 0], [3, 0], [5, 1], [6, 1], [7, 1], [4, 1]], [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [11, 0], [8, 0], [9, 0], [10, 0]], 'Y'])

    def test_parse_ycc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'y')
        self.assertEqual(arr, [[[0, 0], [1, 0], [2, 0], [3, 0], [7, 1], [4, 1], [5, 1], [6, 1]], [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [9, 0], [10, 0], [11, 0], [8, 0]], 'y'])

    def test_parse_rc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'R')
        self.assertEqual(arr, [[[1, 4], [5, 5], [2, 0], [3, 0], [0, 4], [4, 5], [6, 1], [7, 1]], [[7, 1], [1, 0], [2, 0], [3, 0], [0, 1], [5, 0], [6, 0], [8, 1], [4, 1], [9, 0], [10, 0], [11, 0]], 'R'])

    def test_parse_rcc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'r')
        self.assertEqual(arr, [[[4, 4], [0, 5], [2, 0], [3, 0], [5, 4], [1, 5], [6, 1], [7, 1]], [[4, 1], [1, 0], [2, 0], [3, 0], [8, 1], [5, 0], [6, 0], [0, 1], [7, 1], [9, 0], [10, 0], [11, 0]], 'r'])

    def test_parse_oc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'O')
        self.assertEqual(arr, [[[0, 0], [1, 0], [3, 5], [7, 4], [4, 1], [5, 1], [2, 5], [6, 4]], [[0, 0], [1, 0], [5, 1], [3, 0], [4, 0], [10, 1], [2, 1], [7, 0], [8, 0], [9, 0], [6, 1], [11, 0]], 'O'])

    def test_parse_occ(self):
        arr = CUBE_INIT()
        common.parse(arr, 'o')
        self.assertEqual(arr, [[[0, 0], [1, 0], [6, 5], [2, 4], [4, 1], [5, 1], [7, 5], [3, 4]], [[0, 0], [1, 0], [6, 1], [3, 0], [4, 0], [2, 1], [10, 1], [7, 0], [8, 0], [9, 0], [5, 1], [11, 0]], 'o'])

    def test_parse_bc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'B')
        self.assertEqual(arr, [[[4, 2], [1, 0], [2, 0], [0, 3], [7, 2], [5, 1], [6, 1], [3, 3]], [[0, 0], [4, 0], [2, 0], [3, 0], [9, 0], [1, 0], [6, 0], [7, 0], [8, 0], [5, 0], [10, 0], [11, 0]], 'B'])

    def test_parse_bcc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'b')
        self.assertEqual(arr, [[[3, 2], [1, 0], [2, 0], [7, 3], [0, 2], [5, 1], [6, 1], [4, 3]], [[0, 0], [5, 0], [2, 0], [3, 0], [1, 0], [9, 0], [6, 0], [7, 0], [8, 0], [4, 0], [10, 0], [11, 0]], 'b'])

    def test_parse_oc(self):
        arr = CUBE_INIT()
        common.parse(arr, 'O')
        self.assertEqual(arr, [[[0, 0], [1, 0], [3, 5], [7, 4], [4, 1], [5, 1], [2, 5], [6, 4]], [[0, 0], [1, 0], [5, 1], [3, 0], [4, 0], [10, 1], [2, 1], [7, 0], [8, 0], [9, 0], [6, 1], [11, 0]], 'O'])

    def test_parse_occ(self):
        arr = CUBE_INIT()
        common.parse(arr, 'o')
        self.assertEqual(arr, [[[0, 0], [1, 0], [6, 5], [2, 4], [4, 1], [5, 1], [7, 5], [3, 4]], [[0, 0], [1, 0], [6, 1], [3, 0], [4, 0], [2, 1], [10, 1], [7, 0], [8, 0], [9, 0], [5, 1], [11, 0]], 'o'])


class TestHasher(unittest.TestCase):
    def test1(self):
        self.assertTrue(1)
    def test2(self):
        import time
        time.sleep(60)
'''
    def test_corners(self):
        def make_test_list():
            def node(path, remaining):
                if len(remaining) == 1:
                    for x0 in {0, 2, 4}:
                        for x1 in {0, 2, 5}:
                            for x2 in {0, 3, 5}:
                                for x3 in {0, 3, 4}:
                                    for x4 in {1, 2, 4}:
                                        for x5 in {1, 2, 5}:
                                            for x6 in {1, 3, 5}:
                                                
                                                x = [x0,x1,x2,x3,x4,x5,x6]
                                                ret = []
                                                for i in range(7):
                                                    ret.append([int(path[i]), x[i]])
                                                ret.append(['0','0'])
                                                yield ret

                else:
                    for i in remaining:
                        r = copy.deepcopy(remaining)
                        del r[r.index(i)]
                        for ret in node(path + i, r ):
                            yield ret

            for ret in node('', ['0', '1', '2', '3', '4', '5', '6', '7']):
                yield ret

        has_appeared = set()
        for value in make_test_list():
            self.assertFalse( (x := hasher._hash_corners(value)) in has_appeared)
            has_appeared.add(x)

    def test_edges(self):
        def make_test_list():
            def node(path, remaining):
                if len(remaining) == 5:
                    for x0 in {0, 1}:
                        for x1 in {0, 1}:
                            for x2 in {0, 1}:
                                for x3 in {0, 1}:
                                    for x4 in {0, 1}:
                                        for x5 in {0, 1}:
                                            for x6 in {0, 1}:
                                                x = [x0,x1,x2,x3,x4,x5,x6]
                                                ret = []
                                                for i in range(7):
                                                    ret.append([int(path[i]), x[i]])
                                                yield ret
                else:
                    for i in remaining:
                        r = copy.deepcopy(remaining)
                        del r[r.index(i)]
                        p = copy.deepcopy(path)
                        p.append(i)
                        for ret in node(p, r ):
                            yield ret
                
            for ret in node([], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']):
                yield ret

        has_appeared = set()
        for value in make_test_list():
            self.assertFalse( (x := hasher._hash_edges(value, False)) in has_appeared)
            has_appeared.add(x)
'''
class TestIDA(unittest.TestCase):
    def testAstar(self):
        MOVES = ['W','w',
                 'Y','y',
                 'R','r',
                 'O','o',
                 'B','b',
                 'G','g']
        for i in range(100):
            arr = CUBE_INIT()
            mv = ''
            for _ in range(5):
                mv += random.choice(MOVES)
            common.parse(arr, mv)
            self.assertTrue(len(ida.Astar(arr)) <= len(mv))

class TestHumanSolverObject(unittest.TestCase):
    def test_init(self):
        arr = RubiksCube()
        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red, [['r','r','r'],['r','r','r'],['r','r','r']])
        self.assertEqual(arr.orange, [['o','o','o'],['o','o','o'],['o','o','o']])
        self.assertEqual(arr.green, [['g','g','g'],['g','g','g'],['g','g','g']])
        self.assertEqual(arr.blue, [['b','b','b'],['b','b','b'],['b','b','b']])
        self.assertEqual(arr.yellow, [['y','y','y'],['y','y','y'],['y','y','y']])
        
        self.assertEqual(arr.move_list, [])

    def test_turn_white_clockwise(self):
        arr = RubiksCube()
        arr.white = [['x','y','z'],['w','w','w'],['w','w','w']]
        arr.turn_side('W')
        self.assertEqual(arr.white,[['w','w','x'],['w','w','y'],['w','w','z']])
        self.assertEqual(arr.red, [['b','b','b'],['r','r','r'],['r','r','r']])
        self.assertEqual(arr.orange, [['g','g','g'],['o','o','o'],['o','o','o']])
        self.assertEqual(arr.green, [['r','r','r'],['g','g','g'],['g','g','g']])
        self.assertEqual(arr.blue, [['o','o','o'],['b','b','b'],['b','b','b']])
        self.assertEqual(arr.yellow, [['y','y','y'],['y','y','y'],['y','y','y']])

    def test_turn_white_anti(self):
        arr = RubiksCube()
        arr.white = [['x','y','z'],['w','w','w'],['w','w','w']]
        arr.turn_side('w')
        self.assertEqual(arr.white,[['z','w','w'],['y','w','w'],['x','w','w']])
        self.assertEqual(arr.red, [['g','g','g'],['r','r','r'],['r','r','r']])
        self.assertEqual(arr.orange, [['b','b','b'],['o','o','o'],['o','o','o']])
        self.assertEqual(arr.green, [['o','o','o'],['g','g','g'],['g','g','g']])
        self.assertEqual(arr.blue, [['r','r','r'],['b','b','b'],['b','b','b']])
        self.assertEqual(arr.yellow, [['y','y','y'],['y','y','y'],['y','y','y']])

    def test_turn_yellow_clockwise(self):
        arr = RubiksCube()
        arr.yellow = [['x','y','z'],['y','y','y'],['y','y','y']]
        arr.turn_side('Y')
        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red, [['r','r','r'],['r','r','r'],['g','g','g']])
        self.assertEqual(arr.orange, [['o','o','o'],['o','o','o'],['b','b','b']])
        self.assertEqual(arr.green, [['g','g','g'],['g','g','g'],['o','o','o']])
        self.assertEqual(arr.blue, [['b','b','b'],['b','b','b'],['r','r','r']])
        self.assertEqual(arr.yellow, [['y','y','x'],['y','y','y'],['y','y','z']])

    def test_turn_yellow_anti(self):
        arr = RubiksCube()
        arr.yellow = [['x','y','z'],['y','y','y'],['y','y','y']]
        arr.turn_side('y')
        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red, [['r','r','r'],['r','r','r'],['b','b','b']])
        self.assertEqual(arr.orange, [['o','o','o'],['o','o','o'],['g','g','g']])
        self.assertEqual(arr.green, [['g','g','g'],['g','g','g'],['r','r','r']])
        self.assertEqual(arr.blue, [['b','b','b'],['b','b','b'],['o','o','o']])
        self.assertEqual(arr.yellow, [['z','y','y'],['y','y','y'],['x','y','y']])

    def test_turn_red_clockwise(self):
        arr = RubiksCube()
        arr.red = [['x','y','z'],['r','r','r'],['r','r','r']]
        arr.turn_side('R')
        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['g','g','g']])
        self.assertEqual(arr.red, [['r','r','x'],['r','r','y'],['r','r','z']])
        self.assertEqual(arr.orange, [['o','o','o'],['o','o','o'],['o','o','o']])
        self.assertEqual(arr.green, [['g','g','y'],['g','g','y'],['g','g','y']])
        self.assertEqual(arr.blue, [['w','b','b'],['w','b','b'],['w','b','b']])
        self.assertEqual(arr.yellow, [['b','b','b'],['y','y','y'],['y','y','y']])

    def test_turn_red_anti(self):
        arr = RubiksCube()
        arr.red = [['x','y','z'],['r','r','r'],['r','r','r']]
        arr.turn_side('r')
        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['b','b','b']])
        self.assertEqual(arr.red, [['z','r','r'],['y','r','r'],['x','r','r']])
        self.assertEqual(arr.orange, [['o','o','o'],['o','o','o'],['o','o','o']])
        self.assertEqual(arr.green, [['g','g','w'],['g','g','w'],['g','g','w']])
        self.assertEqual(arr.blue, [['y','b','b'],['y','b','b'],['y','b','b']])
        self.assertEqual(arr.yellow, [['g','g','g'],['y','y','y'],['y','y','y']])

    def test_turn_orange_clockwise(self):
        arr = RubiksCube()
        arr.orange = [['x','y','z'],['o','o','o'],['o','o','o']]
        arr.turn_side('O')
        self.assertEqual(arr.white,[['b','b','b'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red, [['r','r','r'],['r','r','r'],['r','r','r']])
        self.assertEqual(arr.orange, [['o','o','x'],['o','o','y'],['o','o','z']])
        self.assertEqual(arr.green, [['w','g','g'],['w','g','g'],['w','g','g']])
        self.assertEqual(arr.blue, [['b','b','y'],['b','b','y'],['b','b','y']])
        self.assertEqual(arr.yellow, [['y','y','y'],['y','y','y'],['g','g','g']])

    def test_turn_orange_anti(self):
        arr = RubiksCube()
        arr.orange = [['x','y','z'],['o','o','o'],['o','o','o']]
        arr.turn_side('o')
        self.assertEqual(arr.white,[['g','g','g'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red, [['r','r','r'],['r','r','r'],['r','r','r']])
        self.assertEqual(arr.orange, [['z','o','o'],['y','o','o'],['x','o','o']])
        self.assertEqual(arr.green, [['y','g','g'],['y','g','g'],['y','g','g']])
        self.assertEqual(arr.blue, [['b','b','w'],['b','b','w'],['b','b','w']])
        self.assertEqual(arr.yellow, [['y','y','y'],['y','y','y'],['b','b','b']])

    def test_turn_blue_clockwise(self):
        arr = RubiksCube()
        arr.blue = [['x','y','z'],['b','b','b'],['b','b','b']]
        arr.turn_side('B')
        self.assertEqual(arr.white,[['w','w','r'],['w','w','r'],['w','w','r']])
        self.assertEqual(arr.red, [['r','r','y'],['r','r','y'],['r','r','y']])
        self.assertEqual(arr.orange, [['w','o','o'],['w','o','o'],['w','o','o']])
        self.assertEqual(arr.green, [['g','g','g'],['g','g','g'],['g','g','g']])
        self.assertEqual(arr.blue, [['b','b','x'],['b','b','y'],['b','b','z']])
        self.assertEqual(arr.yellow, [['y','y','o'],['y','y','o'],['y','y','o']])

    def test_turn_blue_anti(self):
        arr = RubiksCube()
        arr.blue = [['x','y','z'],['b','b','b'],['b','b','b']]
        arr.turn_side('b')
        self.assertEqual(arr.white,[['w','w','o'],['w','w','o'],['w','w','o']])
        self.assertEqual(arr.red, [['r','r','w'],['r','r','w'],['r','r','w']])
        self.assertEqual(arr.orange, [['y','o','o'],['y','o','o'],['y','o','o']])
        self.assertEqual(arr.green, [['g','g','g'],['g','g','g'],['g','g','g']])
        self.assertEqual(arr.blue, [['z','b','b'],['y','b','b'],['x','b','b']])
        self.assertEqual(arr.yellow, [['y','y','r'],['y','y','r'],['y','y','r']])

    def test_turn_green_clockwise(self):
        arr = RubiksCube()
        arr.green = [['x','y','z'],['g','g','g'],['g','g','g']]
        arr.turn_side('G')
        self.assertEqual(arr.white,[['o','w','w'],['o','w','w'],['o','w','w']])
        self.assertEqual(arr.red, [['w','r','r'],['w','r','r'],['w','r','r']])
        self.assertEqual(arr.orange, [['o','o','y'],['o','o','y'],['o','o','y']])
        self.assertEqual(arr.green, [['g','g','x'],['g','g','y'],['g','g','z']])
        self.assertEqual(arr.blue, [['b','b','b'],['b','b','b'],['b','b','b']])
        self.assertEqual(arr.yellow, [['r','y','y'],['r','y','y'],['r','y','y']])

    def test_turn_green_anti(self):
        arr = RubiksCube()
        arr.green = [['x','y','z'],['g','g','g'],['g','g','g']]
        arr.turn_side('g')
        self.assertEqual(arr.white,[['r','w','w'],['r','w','w'],['r','w','w']])
        self.assertEqual(arr.red, [['y','r','r'],['y','r','r'],['y','r','r']])
        self.assertEqual(arr.orange, [['o','o','w'],['o','o','w'],['o','o','w']])
        self.assertEqual(arr.green, [['z','g','g'],['y','g','g'],['x','g','g']])
        self.assertEqual(arr.blue, [['b','b','b'],['b','b','b'],['b','b','b']])
        self.assertEqual(arr.yellow, [['o','y','y'],['o','y','y'],['o','y','y']])

    def test_parse(self):
        arr = RubiksCube()
        parseList = 'WwYyRrOoBbGg'
        arr.parse(parseList)

        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red, [['r','r','r'],['r','r','r'],['r','r','r']])
        self.assertEqual(arr.orange, [['o','o','o'],['o','o','o'],['o','o','o']])
        self.assertEqual(arr.green, [['g','g','g'],['g','g','g'],['g','g','g']])
        self.assertEqual(arr.blue, [['b','b','b'],['b','b','b'],['b','b','b']])
        self.assertEqual(arr.yellow, [['y','y','y'],['y','y','y'],['y','y','y']])

        self.assertEqual(arr.move_list, list(parseList))

    def test_solved(self):
        arr = RubiksCube()
        self.assertTrue(arr.is_solved())
        arr.parse('W')
        self.assertFalse(arr.is_solved())

    def test_scramble(self):
        arr = RubiksCube()
        arr.scramble()
        self.assertFalse(arr.is_solved())


 
class TestHumanSolver(unittest.TestCase):

    def test_daisy(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        self.assertEqual(arr.yellow[0][1], 'w')
        self.assertEqual(arr.yellow[1][0], 'w')
        self.assertEqual(arr.yellow[1][2], 'w')
        self.assertEqual(arr.yellow[2][1], 'w')

    def test_white_cross(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        self.assertEqual(arr.white[0][1], 'w')
        self.assertEqual(arr.white[1][0], 'w')
        self.assertEqual(arr.white[1][2], 'w')
        self.assertEqual(arr.white[2][1], 'w')

        self.assertEqual(arr.red[0][1], 'r')
        self.assertEqual(arr.orange[0][1], 'o')
        self.assertEqual(arr.blue[0][1], 'b')
        self.assertEqual(arr.green[0][1], 'g')

    def test_white_corners(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        solver._white_corners(arr)

        self.assertEqual(arr.white,[['w','w','w'],['w','w','w'],['w','w','w']])
        self.assertEqual(arr.red[0], ['r', 'r', 'r'])
        self.assertEqual(arr.orange[0], ['o', 'o', 'o'])
        self.assertEqual(arr.blue[0], ['b', 'b', 'b'])
        self.assertEqual(arr.green[0], ['g', 'g', 'g'])

    def test_second_layer(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        solver._white_corners(arr)
        solver._second_layer(arr)

        self.assertEqual(arr.red[1], ['r', 'r', 'r'])
        self.assertEqual(arr.orange[1], ['o', 'o', 'o'])
        self.assertEqual(arr.blue[1], ['b', 'b', 'b'])
        self.assertEqual(arr.green[1], ['g', 'g', 'g'])

    def test_yellow_cross(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        solver._white_corners(arr)
        solver._second_layer(arr)
        solver._yellow_cross(arr)

        self.assertEqual(arr.yellow[0][1], 'y')
        self.assertEqual(arr.yellow[1][0], 'y')
        self.assertEqual(arr.yellow[1][2], 'y')
        self.assertEqual(arr.yellow[2][1], 'y')

    def test_solve_cross(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        solver._white_corners(arr)
        solver._second_layer(arr)
        solver._yellow_cross(arr)
        solver._solve_cross(arr)

        self.assertEqual(arr.red[2][1], 'r')
        self.assertEqual(arr.orange[2][1], 'o')
        self.assertEqual(arr.blue[2][1], 'b')
        self.assertEqual(arr.green[2][1], 'g')

    def test_yellow_corners(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        solver._white_corners(arr)
        solver._second_layer(arr)
        solver._yellow_cross(arr)
        solver._solve_cross(arr)
        solver._yellow_corners(arr)

        rb = {arr.yellow[0][2], arr.red[2][2], arr.blue[2][0]}
        bo = {arr.yellow[2][2], arr.orange[2][0], arr.blue[2][2]}
        og = {arr.yellow[2][0], arr.orange[2][2], arr.green[2][0]}
        gr = {arr.yellow[0][0], arr.red[2][0], arr.green[2][2]}

        self.assertEqual(rb, {'r', 'b', 'y'})
        self.assertEqual(bo, {'b', 'o', 'y'})
        self.assertEqual(og, {'o', 'g', 'y'})
        self.assertEqual(gr, {'g', 'r', 'y'})

    def test_yellow_rotations(self):
        arr = RubiksCube()
        arr.scramble()
        solver._daisy(arr)
        solver._white_cross(arr)
        solver._white_corners(arr)
        solver._second_layer(arr)
        solver._yellow_cross(arr)
        solver._solve_cross(arr)
        solver._yellow_corners(arr)
        solver._yellow_rotations(arr)

        self.assertTrue(arr.is_solved())

    def test_solve(self):    
        arr = RubiksCube()
        arr.scramble()

        a = solver.solve(arr)
        self.assertTrue(arr.is_solved())
        self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()
