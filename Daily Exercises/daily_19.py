'''
Given the month and year as numbers, return whether that month contains a Friday 13th.
'''

from datetime import date

def has_friday_13(month, year):
	if date(year, month, 13).weekday() == 4:
		return True
	else:
		return False
