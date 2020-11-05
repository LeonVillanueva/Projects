'''
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one.
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
'''

import numpy as np

def e_frac (n, d):
    d_list = []

    while n != 0:
        x = np.ceil(d/n)
        d_list.append (x)
        n = x*n - d
        d *= x

    return d_list
