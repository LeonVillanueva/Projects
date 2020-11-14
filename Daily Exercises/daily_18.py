'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''

def find_length(n):
    max_length = 0

    while n:
        max_length += 1
        n = n & (n << 1)

    return max_length
