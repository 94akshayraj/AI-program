number = input("enter a number\n")

def lesser(number):
	number = number-1
	print number

	if number == 1:
		return 1
	else:
		lesser(number)
lesser(number)
