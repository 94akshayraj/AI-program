class vect:
	def __init__(self,px,py):
		self.x = px
		self.y = py
	def dispv(self):
		print'(%f,%f)'%(self.x,self.y)
	
	def __add__(self,p):
		newx = self.x+p.x
		newy = self.y+p.y
		newz = newx,newy
		print newz

a = vect(10.5,5.6)
b = vect(5.6,10.5)
a+b
#dispv(v1+v2)