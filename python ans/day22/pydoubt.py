import pandas
from pandas import Series as s
from pandas import DataFrame as df
ser = s('1000,1200,9000,9500,9750'.split(","))
ser.name = 'NAME'
sdf = df(ser)
print sdf
