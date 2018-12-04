import pandas as pd
from pandas import DataFrame as df
import numpy as np

item = ['Laptops','Speakers','Printers','Desktops']*5
place = ['KL']*4+['TN']*4+['KA']*4+['BIHAR']*4+['BENGAL']*4
total = np.random.randint(50,100,20)

dtfr = df({'Items':item,'Places':place,'Total':total})

#print dtfr

while True:
	inp = input('1: Display items. \n2: Display places.\n')
	if inp == 1:
		itm = raw_input('Enter the product name.\n')
		show_item = dtfr[dtfr['Items']==itm]
		totl = show_item['Total']['Places']
		

		print place_in_total