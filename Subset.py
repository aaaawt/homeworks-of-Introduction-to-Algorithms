import numpy as np
from numpy import int32

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Rel = [(2, 8), (9, 4), (2, 9), (2, 1), (2, 5), (6, 2), (5, 9),
       (5, 6), (5, 4), (7, 5), (7, 6), (3, 7), (6, 3)]

# define a matrix
R = np.zeros((len(A), len(A)), dtype=int32)
for x in Rel:
    R[x[0] - 1][x[1] - 1] = 1
    R[x[1] - 1][x[0] - 1] = 1
times = np.sum(R, axis=0)

# define a classification function
def classify(res, num):
    if not res:
        res.append([num + 1])
        return res
    for x in res:
        for y in x:
            if R[y - 1][num] == 1:
                break
        else:
            x.append(num + 1)
            break
    else:
        res.append([num + 1])
    return res

# classify with levels
res = []
level = sorted(set(times), reverse=True)
for ll in level:
    for i, time in enumerate(times):
        if time == ll:
            res = classify(res, i)

print(res)
