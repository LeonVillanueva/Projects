'''
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].
'''

import numpy

def daily_bruteforce (l):
    # assume we checking if list of numeric
    answer = []
    for i in range (len(l)):
        l_new = l.pop(i)
        answer.append (numpy.prod(l_new))
    return answer

def daily_division(l):
    answer = [numpy.prod(l)] * len (l)
    answer = [x/y for x, y in zip(map(int, answer), map(int, l))]
    return answer
