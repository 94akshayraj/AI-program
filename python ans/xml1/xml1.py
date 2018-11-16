import xml.dom.minidom as dm
dtree = dm.parse('/home/ai3/Desktop/common/Python_Exercises/book.xml')
rn = dtree.documentElement
bns = rn.getElementsByTagName('book')
for bn in bns:
	tns = bn.getElementsByTagName('title')
	for tn in tns:
		print tn.nodeName,':',tn.childNodes[0].nodeValue
	ans=bn.getElementsByTagName('author')
	for an in ans:
		print an.nodeName,':',an.childNodes[0].nodeValue
	yrs=bn.getElementsByTagName('year')
	for yr in yrs:
		print yr.nodeName,':',yr.childNodes[0].nodeValue
	prs=bn.getElementsByTagName('price')
	for pr in prs:
		print pr.nodeName,':',pr.childNodes[0].nodeValue
	print '******************************************'


