import pandas as pd
from pandas import Series as s
from pandas import DataFrame as df
import numpy as np

d1 = {'Animals':['Cat','Dog','Cow','Ferret'],'Owners':[1,4,None,1]}
d1 = df(d1)
print d1

#col3 = {'Cage':['No','Yes','No','Yes']}
d1['Cage'] = ['No','Yes','No','Yes']
print d1