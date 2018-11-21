from Tkinter import *
from tkinter import filedialog
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,train_test_split,KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot as plt
import pandas as pd

mwin = Tk()
text = Text(mwin, height=5, width=30).pack()
#fileSelect=Button(mwin,text='Select data file',command=tkFileDialog.askdirectory()).pack()

def fileselect():

	global data
	mwin.filename=filedialog.askopenfilename(initialdir = "/home/ai3/Desktop/common/ML/Day5",title = "Select file",filetypes = (("csv","*.csv"),("all files","*.*")))
	data=pd.read_csv(mwin.filename) 
	text.insert(END,data)

def run_algorithm():
	
#	data=pd.read_csv(filename) 
	data.get()
	
mwin.title('Agl Automator')
mwin.geometry('200x300')
Button(mwin, text='Select data file', command=fileselect).pack()
Button(mwin, text='Run', command=run_algorithm).pack()
mwin.mainloop()


