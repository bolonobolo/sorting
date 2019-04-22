#!/usr/bin/python

# Insertion Sort script
# Best O(n) --> Average O(n^2) --> Worst O(n^2)
import time
import random

def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentvalue
	return alist

# alist = [100, 25, 2, 8, -1, 44]
alist = random.sample(range(1, 100000), 10000)

# print "[*] Unsorted list %s" % (alist)
start = time.time()
nlist = insertionSort(alist)
end = time.time()

# print "[*] Sorted list %s" % (nlist)
print "[*] Script took %s seconds" % (end - start)