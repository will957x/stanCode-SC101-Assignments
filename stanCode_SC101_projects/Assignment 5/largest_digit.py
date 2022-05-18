"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	if n is negative make positive
	returns largest number from n using find_largest_digit_helper
	"""
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, n, n % 10)


def find_largest_digit_helper(n_left, n_right, biggest):
	"""
	brief: returns largest number through bifurcating front and back of n

	specifically splitting n into n_left (contains all digits excluding last) and
	n_right to contain ONLY the last digit
	through repeated bifurcations n will be split into single digits
	each time a single digit is extracted find_largest_digit_helper() will check against the variable holding
	the current biggest digit in biggest variable
	returns biggest digit
	"""
	if n_left == 0:
		pass
	else:
		if n_left < 10:  # keeps checking left of bifurcation against biggest at base case
			biggest = max(n_left, biggest)
			# print(f'biggest from left: {biggest}')  # check if bifurcating left correctly
		if n_right < 10:  # checks right of bifurcation against current biggest
			biggest = max(n_right, biggest)
			# print(f'biggest from right: {biggest}')  # check if bifurcating right correctly
		n_right = n_left  # updates remaining n to bifurcate per round of bifurcation
		return find_largest_digit_helper(n_left//10, n_right % 10, biggest)
	return biggest

# Lilian method
# def find_largest_digit(n):
# 	if n < 0:
# 		n *= -1
# 	if n == 0:
# 		return 0
# 	else:
# 		return max(n % 10, find_largest_digit(n // 10))


if __name__ == '__main__':
	main()
