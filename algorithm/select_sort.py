#!/usr/bin/env python

def findSmallest(arr):
	smallest = arr[0]
	smallestIndex = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallestIndex = i

	return smallestIndex


def selectSort(arr):
	newArr = []
	for i in range(0, len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print selectSort([5, 3, 6, 2, 10])

