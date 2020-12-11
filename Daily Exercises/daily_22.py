'''
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
'''

def fixed_point (x):
    fixed = []
    for i in range(len(x)):
        if i == x[i]:
            fixed.append(x[i])
    if len(fixed) > 0:
        return fixed
    else:
        return False

def fixed_point(array):
    for i in range(len(array)):
        if array[i] == i:
            return i

    return False

# binary search
