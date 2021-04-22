import numpy as np

move_len_arr = np.load('corners.npy')
arr12 = []
for i, x in enumerate(move_len_arr):
    if x == 12:
        arr12.append(i)

np.save('arr12.npy', arr12)
print(len(arr12))

# prints 30
