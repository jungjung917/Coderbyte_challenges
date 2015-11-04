def PrimeTime(num): 
    if num == 1 or num == 2:
        return "true"
    else:
	for i in range(2,num):
	    if num % i == 0:
	        return "false"
	    else:
	        return "true"

print PrimeTime(1)
print PrimeTime(19)  
