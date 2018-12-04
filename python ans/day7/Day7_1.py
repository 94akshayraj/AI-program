class Employee:
	def store(self):
		self.name = raw_input('name ? ')
		self.empno = raw_input('empno ? ')
		self.salary = raw_input('salary ? ')

	def disp(self):
		print 'The employee name is ', name 
		print 'The employee number is ', empno
		print 'The employee salary is ', salary

emp = Employee()
emp.store()
emp.disp()