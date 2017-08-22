#!/usr/bin/env python
try:
	x = input("Enter the 1st number:")
	y = input("Enter the 2ns number:")
	print x/y
except(ZeroDivisionError, TypeError), e:
	print e