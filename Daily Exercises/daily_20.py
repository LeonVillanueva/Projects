'''
Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
'''

def pythogorean (x):
    check = []
    for i in range (3):
        z = x.copy()
        z.append(z.pop(i))
        check.append(z[0]**2 + z[1]**2 - z[2]**2 == 0)
    return sum(check) > 0
