def isRightTriangle (x1,y1,x2,y2,x3,y3): 
	x = ((x1-x3)**2 + (y1-y3)**2) **0.5 
	y = ((x1-x2)**2 + (y1-y2)**2) **0.5 
	z = ((x3-x2)**2 + (y3-y2)**2) **0.5 
	print (x,y,z)

	
	max(x,y,z) 
	x,y,z = sorted ([x,y,z])
	print x**2 + y**2 == z**2

#Return statement = at the end of the function (means that function is done)



isRightTriangle (0,0,3,0,3,4)