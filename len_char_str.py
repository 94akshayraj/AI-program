word = raw_input()
v ='aeiou'
c=0
for i in word:
 if i in v:
  c+=1
if c>=2:
 print c
   
