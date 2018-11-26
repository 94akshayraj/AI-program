class emp:

	def store(self):
		self.name = raw_input("name")
		self.empno = raw_input("empno")
		self.salary = raw_input("salary")

	def display(self):
		print "Name is : %s \nempno is : %s \nsalary is : %s \n " %(self.name,self.empno,self.salary)
E1 = emp()
E1.store()
E1.display()