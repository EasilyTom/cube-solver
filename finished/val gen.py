def make_test_list():
    import copy
    class node():

        def __init__(self, path, remaining):
            
            if len(remaining) == 0:
                global values
                for x0 in range(3):
                    for x1 in range(3):
                        for x2 in range(3):
                            for x3 in range(3):
                                for x4 in range(3):
                                    for x5 in range(3):
                                        for x6 in range(3):
                                            
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
