Write a program (function!) that takes a list and returns a new list that contains all the 
elements of the first list minus all the duplicates.

import random
def main():
	a = [1,1,2,2,3,4,5,3,6,7,4,5,6,7,9,4,3,2,5,3,4]
	b = remove_duplicate(a)
	d = duplicate_dict(a)
	e = duplicate_set(a)
	print b
	print d
	print e
 	
def remove_duplicate(lst):
	c = []
	for i in lst:
		if i not in c:
			c.append(i)
	return c
 	
def duplicate_dict(lst):
	return list(dict([(x,1) for x in lst]).keys())
 
def duplicate_set(lst):
	return list(set([x for x in lst]))

main()
