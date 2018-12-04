class bankAcc():
	noAcc = 0
	dic = dict()
	def set(self):
		self.number = raw_input('Enter acc number: ')
		self.bal = raw_input('Enter balance: ')
		self.typ = raw_input('Enter acc type: ')
		self.name = raw_input('Enter acc name: ')
		self.addr = raw_input('Enter acc address: ')
		# self.number = number
		# self.bal = bal
		# self.typ = typ
		# self.name = name
		# self.addr = addr
		bankAcc.dic[self.number]=[self.bal,self.typ,self.name,self.addr]
		bankAcc.noAcc += 1

	def get(self,accno):
		print bankAcc.dic[accno]
		print '*************************************'
		print 'Details of the account number:',accno
		print 'Available balance:',bankAcc.dic[accno][0]
		print 'Account type:',bankAcc.dic[accno][1]
		print 'Account holder name:',bankAcc.dic[accno][2]
		print 'Account holder address:',bankAcc.dic[accno][3]
		print '*************************************'

		# print bankAcc.dic.values()
 		# print bankAcc.dic.get(self.number)

 	def depo(self,accno):
		print 'Available balance is:',bankAcc.dic[accno][0]
		depo = int(raw_input('Enter amount to be deposited:'))
		bankAcc.dic[accno][0] = depo + int(bankAcc.dic[accno][0])
		print 'Updated available balance is:',bankAcc.dic[accno][0]
		print '*************************************'

	def wd(self,accno):
		print 'Available balance is:',bankAcc.dic[accno][0]
		wd = int(raw_input('Enter amount to be withdrawn:'))
		bankAcc.dic[accno][0] = int(bankAcc.dic[accno][0]) - wd
		print 'Updated available balance is:',(bankAcc.dic[accno][0])
		print '*************************************'

B=bankAcc()
e=0
while e <= 4:
	e = int(raw_input("*************************************\nHow may I help you, Sir?\n1. Add account\n2. See details\n3. Deposit\n4. Withdraw\n5. Exit\nYour selection: "))
	if e == 1:
		B.set()
	elif e== 2:
		e1 = raw_input('Enter the account number:')
		B.get(e1)
	elif e== 3:
		e2 = raw_input('Enter the account number:')
		B.depo(e2)
	elif e==4:
		e3 = raw_input('Enter the account number:')
		B.wd(e3)
	elif e==5:
		exit()
	else:
		print '*************************************'
		print'Invalid selection mister! Enter again.'
		e = 0