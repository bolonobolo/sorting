#!/usr/bin/python

# Insertion Sort script
# Best O(n) --> Average O(n^2) --> Worst O(n^2)

def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentvalue
	return alist

alist = [100, 25, 2, 8, -1, 44]
print "[*] Unsorted list %s" % (alist)
nlist = insertionSort(alist)
print "[*] Sorted list %s" % (nlist)	