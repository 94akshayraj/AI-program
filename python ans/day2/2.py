n1 = input()
n2 = input()
n3 = input()

def greatest(n1,n2,n3):
	if n1 >n2:
		if n1 >n3:
			print 'n1 is greatest'
		else:
			print 'n3 is greatest'
	elif n2>n3:
		print 'n2 is greatest'
	else:
		print 'n3 is greatest'

greatest(n1,n2,n3)