'''
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.
'''

def id_mtrx (x):
    ans = [[0]*abs(x)]*abs(x)
    for i in range (x):
        ans [i][i] = 1
    if x < 0:
        ans = [x.reverse() for x in ans]
    return ans
