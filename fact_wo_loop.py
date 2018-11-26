n1 = raw_input("enter a number\n")
def fact(n1):
	if n1==1:
		return 1
	else:
		return n1*(fact(n1-1))
fact(n1)

