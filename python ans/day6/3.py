import sys

lst = [x *input() for x in range(11)]
f = open("a.txt","w")
for i,x in enumerate(lst):
      a="{} x {} = {}\n".format(i,input(),x)
      print a
      f.write(a)
f.close()

