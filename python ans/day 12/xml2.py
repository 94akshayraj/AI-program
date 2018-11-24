
# coding: utf-8

# In[76]:


import xml.dom.minidom as dm
import pandas as pd

data = pd.read_csv('/home/ai3/python ans/xml1/xml.csv')
doc= dm.Document()
e = doc.createElement('Employee')
doc.appendChild(e)


# In[77]:


for i in range(len(data)):
    e1 =  doc.createElement('EMP')
    e.appendChild(e1)
    e11 = doc.createElement('eno')
    e12 = doc.createElement('ename')
    e13 = doc.createElement('edesig')
    e14 = doc.createElement('esalary')

    t11 = doc.createTextNode(str(data[u'eno'][i]))
    t12 = doc.createTextNode(str(data[u'ename'][i]))
    t13 = doc.createTextNode(str(data[u'edesig'][i]))
    t14 = doc.createTextNode(str(data[u'esalary'][i]))

    e11.appendChild(t11)
    e12.appendChild(t12)
    e13.appendChild(t13)
    e14.appendChild(t14)
    e1.appendChild(e11)
    e1.appendChild(e12)
    e1.appendChild(e13)
    e1.appendChild(e14)


# In[78]:


fd = open('test.xml','w')
e1.writexml(fd,indent='\t',addindent='\t',newl='\n')

