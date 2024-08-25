# Question #4) Write a code snippet that generates the square of every element in the list lst in
# a pythonic way.
# lst = [1, 2, 3, 4]

def square_element(elements_list):
	return [x * x for x in elements_list]


if __name__ == "__main__":
	print(square_element([1,2,3,4]))