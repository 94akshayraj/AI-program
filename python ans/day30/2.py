import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anm

figobj=plt.figure(figsize=(6,6))
subpobj=figobj.add_subplot(111)
x=np.arange(4)
ylabels='sony mi lg asus'.split()
sales=np.array([50,50,50,50])
bars=subpobj.barh(x,sales,align='center')
subpobj.set_xticks(x)
subpobj.set_yticklabels(ylabels)
def animbar(i):
	global bars
	sales=np.array([50,50,50,50])
	print sales
	for bar1,h1 in zip(bars,sales):
		bar1.set_height(h1)
	return bc1
anm1=anm.FuncAnimation(figobj,animbar,interval=3000)
plt.show()
