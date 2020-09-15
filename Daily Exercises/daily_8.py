'''
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.678 is not a palindrome. Do not convert the integer into a string.
'''

def check_palindrome_str(num):
    return str(num) == ''.join(reversed(str(num)))


import math

def check_palindrome_num(num):
    while num % 10 != 0:
        num *= 10
    num = int (num / 10)
    num_c = num

    digits = int(math.log10(num))

    mun = 0

    while digits >= 0:
        mun += (num_c % 10) * (10 ** digits)
        digits -= 1
        num_c = math.floor (num_c/10)

    return num == mun
