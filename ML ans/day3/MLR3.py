from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,cross_val_score
import pandas as pd
import numpy as np


d = pd.read_csv("/home/ai3/Desktop/common/ML/Day3/pimaindians.csv")

data = d.as_matrix()

X = data[:,0:7]
y = data[:,8]



lr = LogisticRegression()
score = cross_val_score(lr,X,y,cv=10)
print(score)