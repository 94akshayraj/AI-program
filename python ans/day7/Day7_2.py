class Employee:
	def __init__(self):
		self.name = raw_input('name ? ')
		self.empno = raw_input('empno ? ')
		self.salary = raw_input('salary ? ')
		print 'The employee name is ', self.name 
		print 'The employee number is ', self.empno
		print 'The employee salary is ', self.salary

emp = Employee()
