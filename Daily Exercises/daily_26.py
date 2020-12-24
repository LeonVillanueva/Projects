'''
Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.
'''
import numpy as np

def visible (x):
    v = 1
    if len (x) > 1:
        for i in range(len(x)-1):
            if x[i+1] > max (x[:i+1]):
                v +=1
    return v

def all_visible (x):
    z = np.transpose (x)
    row = 0
    for i in z:
        if visible (i) == len (i):
            row += 1
    if row == len (x):
        return True
    else:
        return False
