num = input()
	
def fact(num):
	if num != 0:
		num -= 1
		print num
		fact(num)

fact(num)