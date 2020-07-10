def fabricYards (x):
	y = x/360

	y = math.ceil(y)

	return(y)

fabricYards(42)

def isLegalTriangle (a,b,c):
	c>a AND c>b
	if a+b>c: 
		print ("LegalTriangle")
		#max (-- ) = max value i.e.(4,5,6)

