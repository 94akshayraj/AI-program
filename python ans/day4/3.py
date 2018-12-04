sentence = raw_input()

c = 0

d = {}

for i in words:
	if i == i[::-1]:
		c += 1

print c