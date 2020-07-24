def functionName(x): 
	x = x.lower().replace(' ','')  #Immutable
	counter = 0 
	letter = ''
	string = ''
	while len(x) > 0: 
		for word in x: 
			if x.count(word) > counter : 
				counter = x.count(word) 
				letter = word  
			elif x.count (word) == counter and word < letter: 
				letter = word 

		counter = 0
		x = x.replace(letter,'')
		string += letter
		letter = ''
		

	return string 

print functionName ('Greasy Canadian Boys')


def functionName (x): 

	a = x   #Could have just done replace and lower to x without attaching 'a' 
	a = a.replace(' ','')
	a = a.lower()

	# print a
	maxcount = 0 
	maxletter = ''
	newstring = ''
	# print a 

	print 'a'
	while len(a) > 1: 
		for phrase in a: 
			counter = a.count (phrase) 
			# print counter
			# print phrase
			if counter > maxcount: 
				maxcount = counter 
				maxletter = phrase 
			elif counter == maxcount and phrase < maxletter:
				maxletter = phrase 
		newstring += maxletter
		a = a.replace (maxletter,'')
		maxcount = 0 
			



	print newstring
	return newstring 

		
		
print functionName ("I will aaa be old")
frequentDigitFinder( )
def functionName (x):
	for i in 


	"I will attack at dawn"

print functionName ()