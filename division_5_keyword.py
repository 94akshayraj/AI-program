n1 = input('enter a number for divident')
n2 = input('enter a number for divisor')

def div_f(*n):
	n1 = n[0]
	n2 = n[1]
	quotient = n1/n2
	remainder = n1%n2
	print quotient,'and remainder is',remainder

div_f(n1,n2)	
