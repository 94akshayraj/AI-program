class emp:

	def __init__(self):
		self.name = raw_input("name")
		self.empno = raw_input("empno")
		self.salary = raw_input("salary")
		print "Name is : %s \nempno is : %s \nsalary is : %s \n " %(self.name,self.empno,self.salary)
emp()