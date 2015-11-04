"""
the function Division(num1,num2) take both parameters being passed and return the Greatest Common Factor. That is, return the greatest number that evenly goes into both numbers with no remainder. For example: 12 and 16 both are divisible by 1, 2, and 4 so the output should be 4. The range for both parameters will be from 1 to 10^3
"""
def Division(num1,num2):
    factors = list()
    if num1 < num2:
    	temp = num1
	num1 = num2
	num2 = temp
    for i in range(1, int(num2 **0.5) + 1):
	if num2 % i == 0:
            factors.append(i)
	    if i != num2/i:
	        factors.append(num2/i)
    i = 0 
    factors = sorted(factors)
    factor = factors[len(factors)-1]
    while num1 % factor != 0:
	i = i + 1
	factor = factors[len(factors)-1-i]
        
    return factor 
print Division(7,3)
print Division(36,54)

