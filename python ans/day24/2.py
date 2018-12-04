import pandas as pd
from pandas import DataFrame as df
import numpy as np

dafr = df((np.random.randint(10,20,40).reshape(10,4)),columns='c1,c2,c3,c4'.split(','))
# dafr = df(dafr,columns='c1,c2,c3,c4'.split(','))
print dafr

print dafr.sort_values(['c1','c3'],ascending=[True,False])