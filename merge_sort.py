#!/usr/bin/python

# Merge Sort script
# Best O(n log n) --> Average O(n log n) --> Worst O(n log n)
import time
import random


def merge(left, right):
	
	left_index, right_index = 0, 0
	result = []
	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1
	result += left[left_index:]	
	result += right[right_index:]
	return result


def merge_sort(array):
	if len(array) <= 1:
		return array

	# divide array in half and merge sort recursively
	half = len(array) // 2

	left = merge_sort(array[half:])
	right = merge_sort(array[:half])
	return merge(left, right)

# array = [100, 25, 2, 8, -1, 44]
array = random.sample(range(1, 100000), 10000)
# print "[*] Unsorted list %s" % (array)

start = time.time()
narray = merge_sort(array)
end = time.time()

# print "[*] Sorted list %s" % (narray)
print "[*] Script took %s seconds" % (end - start)
