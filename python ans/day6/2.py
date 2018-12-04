import sys
number = input()
lst = [x *number for x in range(11)]
f = open("a.txt","w")
for i,x in enumerate(lst):
      a="{} x {} = {}\n".format(i,number,x)
      print a
      f.write(a)
f.close()
