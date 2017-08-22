#!/usr/bin/env python


def DCFarm(width, length):
	if length % width == 0:
		print width, length
		return;

	tmp = length % width
	if tmp > width:
		length = tmp
	else:
		length = width
		width = tmp
	DCFarm(width, length)

print DCFarm(640, 1680)



def sum(arr):
	if arr == None:
		return 0
	if len(arr) == 1:
		return arr.pop()
	else:
		temp = arr.pop()
		return temp + sum(arr)


print sum([1,2,3,4,5,6,7,4])

def count(list):
	if list == []:
		return 0

	return 1 + count(list[1:])

print count([3,3,3,3,3,3,3])
def max(list):
	if len(list) == 1:
		return list[0]
		#return list[0] if list[0] > list[1] else list[1]
	subMax = max(list[1:])
	return list[0] if list[0] > subMax else subMax

print max([1,2,3,4,25,6,7,4]) 