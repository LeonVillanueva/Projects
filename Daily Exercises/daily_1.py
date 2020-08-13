'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

import numpy

def daily_bruteforce (l, k):
    if isinstance (l, list) and isnumeric(k):
        l = np.array (l)
        for x in range (1,len(l)-1):
            l_roll = np.roll (l, x)
            l_total = l + l_roll
            if k in l_total:
                return True
            else:
                return False
    else:
        print ('Either not a list (l), or non-numeric (k).')

def daily_minus (l, k):
    if isinstance (l, list) and isnumeric(k):
        l = list (set (l))
        l_diff = [k - x for x in l]
        if any (z in l_diff for z in l):
            return True
        else:
            return False
    else:
        print ('Either not a list (l), or non-numeric (k).')
