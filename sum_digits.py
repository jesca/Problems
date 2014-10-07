def sum_digits(num):
	# fill in code for base case scenario:
	if ((num/10) == 0):
		#single digit caes
		return num
	else:
		return sum_digits(num/10) + (num)
