'''
Create a function that takes a number as an argument. Add up all the numbers from 1 to the number you passed to the function. For example, if the input is 4 then your function should return 10 because 1 + 2 + 3 + 4 = 10.
'''

def add_up(num):
	return sum ([i+1 for i in range(num)])

'''
The challenge is to fix all of the bugs in this incredibly messy code, which the code in the image might've actually looked like (probably not)! The code given will output the same middle two lines as in the image shown above.

    First parameter is the user's score.
    Second parameter is the required score.

    Note that inputs will be given as a string percentage number.
    Maintain all capitalization.
    Feel free to declutter and refactor code if it helps!
'''

def grade_percentage(user_score, pass_score):
	u, p = float (user_score.strip('%')), float (pass_score.strip('%'))
	if u<p:
		s='FAILED'
	else:
		s='PASSED'
	return 'You'+' '+s+' '+'the Exam'

'''
Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
Assume all inputs are greater than or equal to 0.
'''

def factorial(num):
  f = 1
  for i in range (1,num+1):
    f *= i
  return f
