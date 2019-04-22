#!/usr/bin/python2.7

# Heap Sort script
# Best O(n log n) (if all keys are distinct, otherwise n) --> Average O(n log n) --> Worst O(n log n)

import time
import random

def max_heapify(array, heaplen, index):
	
	maximum = index
	left = (index * 2) + 1
	right = (index * 2) + 2

	# See if left child of root exists and is 
	# greater than root 
	if left < heaplen and array[index] < array[left]:
		maximum = left
	
	# See if right child of root exists and is 
	# greater than root 
	if right < heaplen and array[maximum] < array[right]:
		maximum = right

	# Change root, if needed 
	if maximum != index:
		array[index], array[maximum] = array[maximum], array[index] # swap
		# Heapify the root
		max_heapify(array, heaplen, maximum)

def heapsize(array):
	return len(array)

def build_max_heap(array):
	heaplen = heapsize(array)
	for index in range(heaplen, -1, -1):
		max_heapify(array, heaplen, index)

def heapsort(array):
	build_max_heap(array)
	# One by one extract elements 
	for index in range(heapsize(array) - 1, 0, -1): 
		array[index], array[0] = array[0], array[index] # swap 
		max_heapify(array, index, 0) 
	return array

# array = [100, 25, 2, 8, -1, 44]
array = random.sample(range(1, 100000), 10000)
# print "[*] Unsorted list %s" % (array)

start = time.time()
narray = heapsort(array)
end = time.time()

# print "[*] Sorted list %s " % (narray)
print "[*] Script took %s seconds" % (end - start)

