"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### DONE

	# Base case: right is less than the left, return -1
	if right < left:
		return -1

	# Get the middle index its value
	middle = (right + left) // 2
	middle_value = mylist[middle]

	# Check if key is less than, greater than, or equal to middle value and act accordingly
	if key < middle_value:
		return _binary_search(mylist, key, left, middle-1)
	elif key > middle_value:
		return _binary_search(mylist, key, middle+1, right)
	else:
		return middle

	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### DONE
	start_time = time.time()
	search_fn(mylist,key)
	end_time = time.time()

	return (end_time - start_time) * 1000
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	# Create output list
	list_of_tuples = []

	# iterate through each tuple
	for size in sizes:
		input_list = list(range(int(size)))
		linear_search_time = time_search(linear_search, input_list, -1)
		binary_search_time = time_search(binary_search, input_list, -1)
		new_tuple = (size, linear_search_time, binary_search_time)
		list_of_tuples.append(new_tuple)
	return list_of_tuples
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

# Calling print results of compare search function:
print_results(compare_search())