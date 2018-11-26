s = raw_input()
c = 0

splee = s.split()

for i in splee:	c+=1 if i[::1] == i[::-1]: else: pass
print c
	









