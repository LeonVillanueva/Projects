'''
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
'''

def rotate(array, k):
    n = len(array) - k
    return array[n:] + array[:n]
