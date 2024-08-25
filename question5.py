# Question #5) Given an integer array nums, write a Python function that returns True if the
# array has duplicates. Otherwise, the function should return False.

def array_duplicates(array):
	return len(array) != len(set(array))



if __name__ == "__main__":
	print(array_duplicates([1,2,3,4]))
	print(array_duplicates([1,2,3,4,2,4]))