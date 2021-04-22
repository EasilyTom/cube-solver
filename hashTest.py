def make_test_list():
    import copy
    class node():

        def __init__(self, path, remaining):
            
            if len(remaining) == 0:
                nonlocal values
                for x0 in {0, 2, 4}:
                    for x1 in {0, 2, 4}:
                        for x2 in {0, 2, 4}:
                            for x3 in {0, 2, 4}:
                                for x4 in {0, 2, 4}:
                                    for x5 in {0, 2, 4}:
                                        for x6 in {0, 2, 4}:
                                            
                                            values.append(path + (str(x0)
                                                                  + str(x1)
                                                                  + str(x2)
                                                                  + str(x3)
                                                                  + str(x4)
                                                                  + str(x5)
                                                                  + str(x6)))

            else:
                for i in remaining:
                    r = copy.deepcopy(remaining)
                    del r[r.index(i)]
                    node(path + i, r )
    values = []

    node('', ['0', '1', '2', '3', '4', '5', '6', '7'])

    return values



def hash_(val):
    """Return the hashed value of a cube state

    val must be a string 8888888866666666"""

    SET_OF_EIGHT_VALUES = ['0', '1', '2', '3', '4', '5', '6', '7']
    def get_num(num):
        val = SET_OF_EIGHT_VALUES.index(num)
        del SET_OF_EIGHT_VALUES[val]
        return val

        
    EIGHTH = 11022480
    SEVENTH = 1574640
    SIXTH = 262440
    FIFTH = 52488
    FOURTH = 13122
    THIRD = 4374
    HALF = 2187
    index = get_num(val[0]) * EIGHTH
    index += get_num(val[1]) * SEVENTH
    index += get_num(val[2]) * SIXTH
    index += get_num(val[3]) * FIFTH
    index += get_num(val[4]) * FOURTH
    index += get_num(val[5]) * THIRD
    index += get_num(val[6]) * HALF

    
    second_half = ''
    
    for x in val[8:15]:
        second_half += str(int(x) // 2)
        
    
    
    index += int(second_half, base=3)

    return index



if __name__ == '__main__':    

    has_appeared = set()

    val_list = make_test_list()
    print('test list made')
    for value in val_list:
        
        if (x := hash_(value)) in has_appeared:
            print(value, x)
            break
        else:
            has_appeared.add(x)
    


