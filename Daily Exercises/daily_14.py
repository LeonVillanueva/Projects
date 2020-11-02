'''
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
'''

def sieve(n):
    is_prime = [False] * 2 + [True] * (n - 1)

    for x in range(n):
        if is_prime[x]:
            for i in range(2 * x, n, x):
                is_prime[i] = False

    for i in range(n):
        if is_prime[i]:
            yield i
