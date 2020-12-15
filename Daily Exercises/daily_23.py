'''
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.
'''
def switch (x):
    if x == ['G','R'] or x == ['B','G']:
        return 'b'
    if x == ['B','R'] or x == ['R','B']:
        return 'r'
    if x == ['G','B'] or x == ['B','G']:
        return 'r'

def pass_thru (x):
    n = len (x)
    while n > 1:
        z

COLORS = {'R', 'G', 'B'}

def transform(a, b):
    return list(COLORS - {a, b})

def num_remaining(quxes):
    if len(set(quxes)) == 1:
        return len(quxes)

    results = []
    for i, pair in enumerate(zip(quxes, quxes[1:])):
        if pair[0] != pair[1]:
            results.append(num_remaining(quxes[:i] + transform(*pair) + quxes[i + 2:]))

    return min(results)
