def MultiplicativePersistence(num): 
    times = 1
    if num < 10:
        return 0
    else: 
        while num  >= 10:
            if num % 10 == 0:
	        times = times
	    else:
	        times *= (num % 10)     
	    num = num // 10
        times = times * num
        return 1 + MultiplicativePersistence(times)

print MultiplicativePersistence(25)
