def pch(cn,n=0):
	print '-'*n,cn.__name__
	for scn in cn.__subclasses__():
		pch(scn,n+6)
pch(BaseException)