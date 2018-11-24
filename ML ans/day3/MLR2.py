from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error

d = pd.read_csv("/home/ai3/Desktop/common/ML/Day3/loan.csv")

data = d.as_matrix()

X = data[:,(0,1)]
y = data[:,2]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

lr = LinearRegression()

lr.fit(X_train,y_train)

p = lr.predict(X_test)

print(mean_absolute_error(y_test,p))
print(mean_squared_error(y_test,p))
print(np.sqrt(mean_squared_error(y_test,p)))