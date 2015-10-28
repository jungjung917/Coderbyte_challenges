def PowersofTwo(num): 
    if num == 0:
    	return "false"
    elif num % 2 != 0:
    	return "false"
    else: 
    	if num // 2 == 1 :
            return "ture"
        else: 
	    return PowersofTwo(num // 2)
				    
				        
					# keep this function call here  
					# to see how to enter arguments in Python scroll down
					
print PowersofTwo(128) 
