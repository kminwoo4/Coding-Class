#Question 1 

sumOfAll = 0 

for i in range (1,21): 
	sumOfAll = sumOfAll + i 
	print sumOfAll
#This is not a function; this is a loop 

#THat is why sumOFAll = the actual value, not the global variable 

#Question 2 

JesusChrist = 0
for z in range (1,101): 
	if (i % 3 == 0 or i % 5 == 0) : 
		JesusChrist = JesusChrist + i 

print JesusChrist

def sumFromMtoN(m,n):
	MrLahey = 0 
	for g in range (m,n):
		MrLahey = MrLahey + g 
	return MrLahey
	
	
print sumFromMtoN(5,19)


def getKthDigit (n,k) : 
	return n/(10**k)%10

getKthDigit (789,0) 



#hint: 789 
