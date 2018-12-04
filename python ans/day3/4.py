inp_str = raw_input()
vowels = 'aeiouAEIOU'
 
c = 0

for i in inp_str:
	if i in vowels:
		c += 1
	else:
		pass

print c>=2
