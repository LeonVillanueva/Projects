'''
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
'''

def fib (n):
    if n == 0:
        x = 0
    elif n == 1:
        x += 1
    else:
        x = 1
        for i in range (n-2):
            x += x
    return x

def fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
