#!/usr/bin/python2.7

# QuickSort script
# Best O(n log n) --> Average O(n log n) --> Worst O(n^2)

import random
import time

def partition(array, pivot, rest):
	
	x = array[rest]
	i = pivot - 1 
	for j in range(pivot, rest):
		 if array[j] <= x:
		 	i = i + 1
		 	array[i], array[j] = array[j], array[i]
	array[i+1], array[rest] = array[rest], array[i+1]
	return i+1

def quicksort(array, pivot, rest):

	if pivot < rest:
		q = partition(array, pivot, rest)
		quicksort(array, pivot, q - 1)
		quicksort(array, q + 1, rest)

	return array

# array = [100, 25, 2, 8, -1, 44]
array = random.sample(range(1, 100000), 10000)
# print "[*] Unsorted list %s" % (array)

start = time.time()
narray = quicksort(array, 0, len(array) - 1)
end = time.time()

# print "[*] Sorted list %s " % (narray)
print "[*] Script took %s seconds" % (end - start)