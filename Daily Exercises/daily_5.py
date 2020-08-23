'''
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

from random import uniform
from math import pow

def generate():
    return (uniform(-1, 1), uniform(-1, 1))

def is_in_circle(coords):
    return coords[0] * coords[0] + coords[1] * coords[1] < 1

def estimate():
    iterations = 10000000
    in_circle = 0
    for _ in range(iterations):
        if is_in_circle(generate()):
            in_circle += 1
    pi_over_four = in_circle / iterations
    return pi_over_four * 4
