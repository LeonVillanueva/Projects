'''
You are given an array representing the heights of neighboring buildings on a city street, from east to west. The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
'''

def sunset (x):
    i = -len(x)
    sun = []
    while i != -1:
        west = x[i+1:]
        sun.append (x[i] > max (west))
        i += 1
    return sum (sun) + 1
