class bankAcc():
	noAcc = 0
	dic = dict()
	def set(self):
		self.number = raw_input('Enter acc number: ')
		self.bal = raw_input('Enter balance: ')
		self.type = raw_input('Enter acc type: ')
		self.name = raw_input('Enter acc name: ')
		self.addr = raw_input('Enter acc address: ')
		bankAcc.dic[self.number]=[self.bal,self.type,self.name,self.addr]
		bankAcc.noAcc += 1

	# def get(self):


B=bankAcc()
e=0
while e < 4:
	e = int(raw_input("What would you like to know, Sir?\n1. Add account\n2. See details\n3. Deposit\n4. Withdraw\n5. Exit\nYour selection: "))
	if e == 1:
		B.set()