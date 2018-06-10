def expRecur(base, exp):
	
	if(exp == 0):
		return 1
	else:
		return base * expRecur(base, exp-1)