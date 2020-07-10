def absVal (s):
	if type(s) != int:
		pring('Not an Integer')

	if s < 0: #negative value 
		s = -s #equal to c*(-1)	

	return s

print absVal(10)
print absVal(-10)
print absVal('s')