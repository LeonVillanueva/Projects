'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

def daily_bruteforce(lst):
    if (all(isinstance(x, int) for x in lst)):
        lst_new = list (set([x for x in lst if x>0]))
        for i in range (max (lst_new)):
            if (max (lst_new) - i) not in lst_new:
                return (max (lst_new) - i)
            if (max (lst_new) == i):
                return (max (lst_new) + 1)
    else:
        print ('not all integers')

'''
Sorting takes O(n log n), so we can't use that here.
'''

def daily_simple(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i

def daily_reverse(nums):
    p = [x for x in nums if (x > 0)]
    r = reverse (set (p))
    l = len (r)
    m = max (r)
    if l == r:
        return m + 1
    else:
        while l > 0:
            l -= 1
            if m - 1 not in r:
                return m - 1
            else:
                m -= 1
