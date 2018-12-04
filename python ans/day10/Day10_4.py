def div(**num):
	q = num['div'] / num['dis']
	r = num['div']% num['dis']
	return q,r
try:
	a = input()
	b = input()
	x,y = div(div=a,dis=b)

except:
	print'error 0  HAHAHA'

else:
	print x,y	
	
finally:
	print 'success' 