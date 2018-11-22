import abc

class employee:
	__metaClass__=abc.ABCMeta	
	def __init__(self,name,no,bp):
		self.name = name
		self.no = no
		self.bp = bp
		self.da =  self.bp * .3
		self.hra = self.bp * .1
		self.sp = 0

	def show(self):
		print 'name is ',self.name
		print 'emp no is ',self.no
		print 'basic pay is ',self.bp
		print 'direct allowance  ', self.da
		print 'hr allowance  ', self.hra
		print 'sp allowance  ', self.sp
	@abc.abstractmethod
	def calchra(self):
		pass

	def calcsp(self):
		pass

class engg(employee):
	def calcsp(self):
		self.sp = self.bp*.2

class jengg(engg):
	def calca(self):
		self.hra+=500

class sengg(engg):
	def calca(self):
		self.hra+=1000

class officer(employee):
	def calcsp(self):
		self.sp = self.bp*.1

A=officer("Varun",111,10000)
B=jengg("Shibin",122,15000)
C=sengg("Tom",133,20000)
A.calchra()
B.calchra()
C.calchra()
A.calcsp()
B.calcsp()
C.calcsp()
A.show()
B.show()
C.show()