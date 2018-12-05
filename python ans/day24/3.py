from pandas import DataFrame as f
import numpy as np
import random
item=['Laptops','Printers','Speakers','Desktops']*5
place=['KL']*4+['TN']*4+['KA']*4+['BIHAR']*4+['BENGAL']*4
total=random.sample(range(10,50),20)
df=f({'Items':item,'Places':place,'Total':total})
print df,"\n\n"
while True:
	x=input("\n1.Display Placewise Rank \n2.Display Itemwise Rank \n3.Exit\n>")
	if x==1:
		it=raw_input()
		il=df[df['Items']==it]
		il=il.copy()
		tol=il['Total']
		rank=tol.rank(ascending=True)
		il['Rank']=rank
		print il
	elif x==2:
		p=raw_input("Enter the place Name : ")
		pl=df[df['Places']==p]
                pl=pl.copy()
                tol=pl['Total']
                rank=tol.rank(ascending=True)
                pl['Rank']=rank
                print pl
	else:
		break