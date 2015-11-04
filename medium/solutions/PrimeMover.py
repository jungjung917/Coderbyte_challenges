"""
the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. For example: if num is 16 the output should be 53 as 53 is the 16th prime number. 
"""

"""
##solution1
import math
def PrimeMover(num):
    Prime_numbers = [2]   
    for i in range(3, 10000):
        isprime = list()
	for n in range(2,int(math.sqrt(i)+1)):
            if i % n == 0: 
	       isprime.append(False)
	    else: 
	       isprime.append(True)
	if all(isprime):
	    Prime_numbers.append(i)
    return Prime_numbers[num-1]
"""
## solution 2:
import time
def PrimeMover(num):
    prime_num = 2
    i = 2
    while num > 1:
        i = i + 1
	isprime = 0
	for n in xrange(2,int(i**0.5)+1):
	    if i % n == 0:
	        isprime += 1
        
	if isprime == 0:
            prime_num = i
            num = num - 1
    return prime_num
print time.time()
print PrimeMover(2)
print time.time()
print PrimeMover(567)
print time.time()

