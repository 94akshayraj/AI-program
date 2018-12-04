#!/usr/bin/python
from Tkinter import *
mwin=Tk()
vexp=''

def bhan(ch):
	global vexp
	if ch =='ce':
		 vexp = ''
	elif ch == '=':
		vexp = str(eval(vexp))
	else:
		vexp += ch
	t1.set(str(vexp))

mwin.title('calc')
mwin.geometry('245x365')

t1=StringVar()
e1=Entry(mwin,textvariable=t1)
b1=Button(mwin,text='7',command=lambda:bhan('7'),width=5,height=5)
b2=Button(mwin,text='8',command=lambda:bhan('8'),width=5,height=5)
b3=Button(mwin,text='9',command=lambda:bhan('9'),width=5,height=5)
b4=Button(mwin,text='4',command=lambda:bhan('4'),width=5,height=5)
b5=Button(mwin,text='5',command=lambda:bhan('5'),width=5,height=5)
b6=Button(mwin,text='6',command=lambda:bhan('6'),width=5,height=5)
b7=Button(mwin,text='1',command=lambda:bhan('1'),width=5,height=5)
b8=Button(mwin,text='2',command=lambda:bhan('2'),width=5,height=5)
b9=Button(mwin,text='3',command=lambda:bhan('3'),width=5,height=5)
b0=Button(mwin,text='0',command=lambda:bhan('0'),width=5,height=5)

bp=Button(mwin,text='+',command=lambda:bhan('+'),width=5,height=5)
bm=Button(mwin,text='-',command=lambda:bhan('-'),width=5,height=5)
bmlt=Button(mwin,text='x',command=lambda:bhan('*'),width=5,height=5)
bd=Button(mwin,text='/',command=lambda:bhan('/'),width=5,height=5)

bf=Button(mwin,text='.',command=lambda:bhan('.'),width=5,height=5)
bc=Button(mwin,text='CE',command=lambda:bhan('ce'),width=5,height=5)
be=Button(mwin,text='=',command=lambda:bhan('='),width=10,height=10)

e1.grid(row=0,column=0,columnspan=9)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b0.grid(row=4,column=1)

bp.grid(row=1,column=3)
bm.grid(row=2,column=3)
bmlt.grid(row=1,column=4)
bd.grid(row=2,column=4)

bf.grid(row=4,column=2)
bc.grid(row=4,column=0)
be.grid(row=3,column=3,columnspan=2,rowspan=2)

mwin.mainloop()
