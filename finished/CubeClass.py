class Cube:
    def __init__(self):
        self.corners = [[0, 0], [1, 0], [2, 0], [3, 0],[4, 1], [5, 1], [6, 1], [7, 1]]
        # wrb, wrg, wog, wob, yrb, yrg, yog, yob
        # second value is which way its w/y sticker is facing wyrobg 012345
    def turn_white(self, prime=False):
        # wrb -> wrg -> wog -> wob
        # prime: wob -> wog -> wrg -> wrb
        if prime:
            self.corners[0], self.corners[1], self.corners[2], self.corners[3] = self.corners[1], self.corners[2], self.corners[3], self.corners[0]
            for num in {1, 2, 3, 4}:
                corner = self.corners[num][1]
                if corner == 2: # red
                    self.corners[num][1] = 4
                elif corner == 3: # orange
                    self.corners[num][1] = 5
                elif corner == 4: # blue
                    self.corners[num][1] = 3
                elif corner == 5: # green
                    self.corners[num][1] = 2
        else:    
            self.corners[1], self.corners[2], self.corners[3], self.corners[0] = self.corners[0], self.corners[1], self.corners[2], self.corners[3]
            for num in {1, 2, 3, 4}:
                corner = self.corners[num][1]
                if corner == 2: # red
                    self.corners[num][1] = 5
                elif corner == 3: # orange
                    self.corners[num][1] = 4
                elif corner == 4: # blue
                    self.corners[num][1] = 2
                elif corner == 5: # green
                    self.corners[num][1] = 3
                
    def turn_yellow(self, prime=False):
        # yrb -> yob -> yog -> yrg
        if prime:
            self.corners[4], self.corners[5], self.corners[6], self.corners[7] = self.corners[7], self.corners[4], self.corners[5], self.corners[6]
            for num in {4, 5, 6, 7}:
                corner = self.corners[num][1]
                if corner == 2: # red
                    self.corners[num][1] = 5
                elif corner == 3: # orange
                    self.corners[num][1] = 4
                elif corner == 4: # blue
                    self.corners[num][1] = 2
                elif corner == 5: # green
                    self.corners[num][1] = 3
        else:
            self.corners[4], self.corners[5], self.corners[6], self.corners[7] = self.corners[5], self.corners[6], self.corners[7], self.corners[4]
            for num in {4, 5, 6, 7}:
                corner = self.corners[num][1]
                if corner == 2: # red
                    self.corners[num][1] = 4
                elif corner == 3: # orange
                    self.corners[num][1] = 5
                elif corner == 4: # blue
                    self.corners[num][1] = 3
                elif corner == 5: # green
                    self.corners[num][1] = 2
    def turn_red(self, prime=False):
        # wrb -> yrb -> yrg -> wrg
        if prime:
            self.corners[0], self.corners[4], self.corners[5], self.corners[1] = self.corners[4], self.corners[5], self.corners[1], self.corners[0]
            for num in {0, 1, 4, 5}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 5
                elif corner == 5: # green
                    self.corners[num][1] = 1
                elif corner == 1: # yellow
                    self.corners[num][1] = 4
                elif corner == 4: # blue
                    self.corners[num][1] = 0
                
        else:
            self.corners[0], self.corners[4], self.corners[5], self.corners[1] = self.corners[1], self.corners[0], self.corners[4], self.corners[5]
            for num in {0, 1, 4, 5}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 4
                elif corner == 5: # green
                    self.corners[num][1] = 0
                elif corner == 1: # yellow
                    self.corners[num][1] = 5
                elif corner == 4: # blue
                    self.corners[num][1] = 1

    def turn_orange(self, prime=False):
        if prime:
            self.corners[2], self.corners[3], self.corners[6], self.corners[7] = self.corners[6], self.corners[2], self.corners[7], self.corners[3]
            for num in {2, 3, 6, 7}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 4
                elif corner == 5: # green
                    self.corners[num][1] = 0
                elif corner == 1: # yellow
                    self.corners[num][1] = 5
                elif corner == 4: # blue
                    self.corners[num][1] = 1
        else:
            self.corners[2], self.corners[3], self.corners[6], self.corners[7] = self.corners[3], self.corners[7], self.corners[2], self.corners[6]
            for num in {2, 3, 6, 7}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 5
                elif corner == 5: # green
                    self.corners[num][1] = 1
                elif corner == 1: # yellow
                    self.corners[num][1] = 4
                elif corner == 4: # blue
                    self.corners[num][1] = 0

    def turn_blue(self, prime=False):
        if prime:
            self.corners[0], self.corners[3], self.corners[4], self.corners[7] = self.corners[3], self.corners[7], self.corners[0], self.corners[4]
            for num in {0, 3, 4, 7}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 2
                elif corner == 3: # orange
                    self.corners[num][1] = 0
                elif corner == 1: # yellow
                    self.corners[num][1] = 3
                elif corner == 2: # red
                    self.corners[num][1] = 1
        else:
            self.corners[0], self.corners[3], self.corners[4], self.corners[7] = self.corners[4], self.corners[0], self.corners[7], self.corners[3]
            for num in {0, 3, 4, 7}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 3
                elif corner == 3: # orange
                    self.corners[num][1] = 1
                elif corner == 1: # yellow
                    self.corners[num][1] = 2
                elif corner == 2: # red
                    self.corners[num][1] = 0

    def turn_green(self, prime=False):
        if prime:
            self.corners[1], self.corners[2], self.corners[5], self.corners[6] = self.corners[5], self.corners[1], self.corners[6], self.corners[2]
            for num in {1, 2, 5, 6}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 3
                elif corner == 3: # orange
                    self.corners[num][1] = 1
                elif corner == 1: # yellow
                    self.corners[num][1] = 2
                elif corner == 2: # red
                    self.corners[num][1] = 0
        else:
            self.corners[1], self.corners[2], self.corners[5], self.corners[6] = self.corners[2], self.corners[6], self.corners[1], self.corners[5]
            for num in {1, 2, 5, 6}:
                corner = self.corners[num][1]
                if corner == 0: # white
                    self.corners[num][1] = 2
                elif corner == 3: # orange
                    self.corners[num][1] = 0
                elif corner == 1: # yellow
                    self.corners[num][1] = 3
                elif corner == 2: # red
                    self.corners[num][1] = 1
                    
    def parse(self, string):
        MOVES = {'w': self.turn_white,
                 'y': self.turn_yellow,
                 'r': self.turn_red,
                 'o': self.turn_orange,
                 'b': self.turn_blue,
                 'g': self.turn_green,
                 }
        for i in string: 
            MOVES[i.lower()](i.islower())
            
            
if __name__ == '__main__':
    arr = Cube()
    arr.parse('wYrG')
    print(arr.corners)
