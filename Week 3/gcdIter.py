def expRecur(a, b):
	
	while(b != 0):
		b = a%b
		(a,b) = (b,a)