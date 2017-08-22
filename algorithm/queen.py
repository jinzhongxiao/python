#!/usr/bin/env python
import random
def queens(num = 8, state=()):
	result = []
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num -1:
				yield (pos,)
			else:
				for result in queens(num, state+(pos,)):
					yield  result +(pos,) 


def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i] - nextX) in (0, nextY - i):
			return True
	return False

def prettyprint(solution):
	def line(pos, length = len(solution)):
		return '.'*(pos) + "X" + '.'*(length -1 -pos)
	for pos in solution:
		print line(pos)

prettyprint(random.choice(list(queens(8))))