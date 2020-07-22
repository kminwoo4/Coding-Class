# def absolutevalue (x):
# 	if type(x) == int:
# 		print("It is an integer")
# 	if x>0:
# 		print("true")
# 	if x<0:
# 		print ("false")
# x=absolutevalue(100) 

# def trianglePattern (x): 
# 	rows = int(input(4))
	# k = 0 
	# for i in range (1,rows +1): 
	# 	for j in range (1, (rows - i) +1): 
	# 		print ("")
	# 		print ("*") while k! = (2*i-1)

	# k = 2 
	# m = 1 
	# for i in range (1, rows): 
	# 	for j in range (1, k): 
	# 		print (" ")
	# 	if m <= (2 * (rows -i) - 1): 
	# 		print ("*", end = " ")

# def square (rows): 
# 	for i in range (rows):  #range from 0-2 (upper part) #since I is the range of rows, have to -1 
# 		print (''*(rows - i - 1) + '* '*(i + 1)) #after space, there is no space for star 
# 	for j in range (rows -1,0,-1): 
# 		print (''*(rows - j) + '* '*(j))
# print square (4) 

#New Concepts 
#Last time we covered list (at least half of it )
#Strings is for Today (7/22)

# print 'asdf'
# a = 'asdf' #Allocating string to a variable 
# print a 
# print len (a)


# bigWord = "ABCD"
# smallWord = 'abcd'
# print bigWord.lower()
# print smallWord.upper()
# bigWord = #Have to assign 
#mutable = LIST
#immutable = STRING and INTEGER are IMMUTABLE (EXAMPLE UP THERE)

# a = ['apple', 'banana'] #with list, you dont have to do a = (); will automatically change (pop,remove, append)
# a.append ('pear')
# print a 

# #integer is "IMMUTABLE"
# b = 38 
# b = b+7 
# print b 

# #WORD "IN" *** 
# a = 'string'
# print 'ring' in a 
# print 'bring' in a
# print 'bring' not in a 

# #INDEXING (YOU CAN INDEX THE STRING)

# print a[0]
# print a[3]
# # print a[6] #THIS one is ERROR 
# print a[-1]
# print a[0:3] #Similar to "FOR" Loop; doesnt include the 3rd. 
# print a[0:5:2] #Increasinb by 2 

# for i in range (0,len(a)): 
# 	print i
# 	print [i]
# #SIMPLER WAY 
# for i in a: 
# 	print i #GO through the entire string i=a

# def palindrome (s):  #Reverse order of the word is the same 
# 	return s == s [:: -1]

# print palindrome ('racecar')

# #chr and ord .... ASCII Characters / Numbers 
# print 'a' > 'A'
# print 'b' > 'c'		#Table containing ASCII numbers (tables)
# print ord('A')
# print ord('a')		#Conversion from ASCII to characters 
# print chr(97)		#Alphabets or symbols have numerical values attached to them
# print chr(65)		#No need to memorize the values 

# a = '    I am Bob. I am Bob. I am 6    ' #spaces trailing spaces #GETTING RID OF SPACES 

# print a 
# print a.strip()
# print a.replace ('Bob', 'Jill')
# print a.replace('Bob','Jill',1) #give it a count 
# print a.count ('Bob')
# print a.startswith("I am")
# print a.endswith(' ')
# print a.find ('am') #finds the first INDEX of where "am" is 
# print a.index('am')


# b = "Minki is 49 years old"

# print b 
# print b.find ("is")
# print b.endswith('old') 

#QUESTIONNNN : Hard one I guess 
# def frequentDigitFinder (x): 
# 	a = x 
# 	a = a.replace(' ','')
# 	a = a.lower()
# 	print a
# print frequentDigitFinder ('What is up')

# continue 

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
# frequentDigitFinder( )
# def functionName (x):
# 	for i in 


	#"I will attack at dawn"

# print functionName ()


