class employee:
	def __init__(self,name,empno,basic_pay):
		self.name = name
		self.empno = empno
		self.basic_pay = basic_pay

	def disp(self):
		print ' the name is %s and pay is %s' %(self.name,self.basic_pay)


class scientist(employee):
	def __init__(self,name,basic_pay,tech_pay,category):
		employee.__init__(self,name,basic_pay)
		self.tech_pay = tech_pay
		self.category = category
		
	def disps(self):
		print 'the name is %s and pay is %s \nthe allowance is %s and category is %s' %(self.name,self.basic_pay,self.tech_pay,self.category)


class officer(employee):
	def __init__(self,grade,department,name,basic_pay):
		employee.__init__(self,name,basic_pay)
		self.grade = grade
		self.department = department

	def dispo(self):
		print 'the name is %s and pay is %s \n the grade is %s and department is %s' %(self.name,self.basic_pay,self.grade,self.department)


n1 = raw_input('name')
p1 = raw_input('pay')
a1 = raw_input('allowance')
c1 = raw_input('category')

s1 = scientist(n1,p1,a1,c1)
#s2 = officer(n1,p1,)
s1.disps()
