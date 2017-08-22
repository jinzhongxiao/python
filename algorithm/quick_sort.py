#!/usr/bin/env python

def quickSort(arr):
	if len(arr) < 2:
		return arr
	pivot = arr[0]
	less = [i for i in arr[1:] if i <= pivot]
	great = [i for i in arr[1:] if i > pivot]

	return quickSort(less) + [pivot] + quickSort(great)

print quickSort([10,5 ,2,3])