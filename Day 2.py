def isEquilateralTriangle (x,y,z):
	if x==y==z: 
		print("True")
	else:
		print("False")
	return x,y,z
print isEquilateralTriangle(5,5,5)

def isEquilateralTriangle (x,y,z):
	print (x==y==z)
	print (type(y)) #boolean (true or false/ yes or no)/ comparing (3>5)
isEquilateralTriangle (5,3,3)

def isPerfectSquare (n): 
	if (type (n**2)== int):
		print("true")
isPerfectSquare(25)

def isPerfectSquare(n):
	print (n == int(n**0.5)**2) #I am typecasting.. then... #Boolean == the same thing
isPerfectSquare(36)

import math 

def isPerfectSquare (n):
	print math.sqrt(n)
isPerfectSquare(36)


#3 Types of Errors -- Topic 
#1. Syntax Error = Compile - Time Error *******
#Grammer Error = like without period at the end of sentence (forgot something)
print ("U")
#2 RunTime Error (crash)
print(1/0) #Simply a division by Zero Error 

#Logical Error (Compiles and Runs but is just wrong )
#i.e.  
print("2+2=5"). #works but not right 

#Subject 2 - Loop 1 (For Loop)
for i in range (1,99):
	print i
	#from the first index to the last index (1-99), print everything from the beginning to the last 
	#don't count the last one (1,98)
#Structure of "for"
	for counter(name) in (range) #needs to stick with to the body 