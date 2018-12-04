sentence = raw_input()

c = 0

words = sentence.split()

for i in words:
	if i == i[::-1]:
		c += 1

print c