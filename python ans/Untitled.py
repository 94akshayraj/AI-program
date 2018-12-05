
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame as df


# In[2]:


def initialize():
	df = np.dtype([('empname','S20'),('empno','i8'),('empdesig','S10'),('empsalary','f8'),('empph','S10')])
	data = np.loadtxt('/home/ai3/Desktop/common/Python_Exercises/emp.csv',delimiter=',',dtype=df)
	data = pd.read_csv('/home/ai3/Desktop/common/Python_Exercises/emp.csv', sep=',')
	data = data.as_matrix
	print data

# In[3]:

# In[4]:


def add():
	aempname = raw_input()
	aempno = input()
	aempdesig = raw_input()
	aempsalary = input()
	aempph = input()
	datlist = [(aempname,aempno,aempdesig,aempsalary,aempph)]
	#type(datlist)
	
	aemp = np.array(datlist,dtype=df)
	data_final = np.concatenate([data,aemp],axis=0)
	print data_final
	

# In[5]:






# In[6]:


def delete():
	n = np.where(data==data[data['empno']==input('Enter employee number to fire him/her.')])
	data = np.delete(data, n)
	print data


# In[12]:


def dispname():
	disp_data = input('Enter employee name/number to see her/his record.')
	if type(disp_data) == str:
    		print data[data['empname']==disp_data]
	else:
		print data[data['empno']==disp_data]
#data[(data['empno'] data['empname'])==input('Enter employee name/number to see her/his record.')]
#date


# In[15]:


def disp():
	print data


# In[17]:


def save():
	data.to_csv('emp_reloded.csv')


# In[ ]:


def exit():
	exit()


# In[ ]:


def menu():
    print 'High priority confidential record maintenance systems and Co.'
    print '1.Initialize '
    print '2. Add record?'
    print '3. Delete record?'
    print '4. Display record by name?'
    print '5. Display record in all?'
    print '6. Save all'
    print '7. Exit'
    
    loop = True
    choice = input('Enter your choice: ')

    while loop == True:
        if choice == 1:
            initialize()
        elif choice == 2:
            add()
        elif choice == 3:
            delete()
        elif choice == 4:
            dispname()
        elif choice == 5:
            disp()
        elif choice == 6:
            save()
        elif choice == 7:
            exit()
        else:
            loop = False
menu()    

