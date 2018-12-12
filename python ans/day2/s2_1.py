
num = input()
def descen(num):
	
	if num !=0:
		num -=1
		print num
		descen(num)
	
descen(num)