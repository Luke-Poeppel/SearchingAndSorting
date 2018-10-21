'''
Binary Search Algorithm with sorted-verification helper function.
'''

def check_if_sorted(lst):
	'''
	Uses recursion to check if a an input list is sorted

	>>> l1 = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9]
	>>> l2 = [100, 101, 102, 103, 104, 105, 106, 107, 108]
	>>> print(check_if_sorted(l1))
	False
	>>> print(check_if_sorted(l2))
	True
	'''
	if (type(lst) != list):
		raise Exception("Input must be a sorted list and search value.")

	if (len(lst) == 1):
		return True
	else:
		remainder = check_if_sorted(lst[1:])
		return (lst[0] <= lst[1] and remainder)

def iterative_binary_search(std_lst, search_val):
	'''
	Iterative Binary Search Algorithm.
	Requires a sorted list as input.

	>>> l3 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
	>>> print(iterative_binary_search(l3, 12))
	True
	'''
	first = 0
	last  = (len(std_lst) - 1)
	found = False

	while (first <= last and not found):
		midpoint = (first + last) // 2
		if (std_lst[midpoint] == search_val):
			found = True
		else:
			if (std_lst[midpoint] > search_val):
				last = (midpoint - 1)
			else:
				first = (midpoint + 1)

	return found

if __name__ == '__main__':
	import doctest
	doctest.testmod()
