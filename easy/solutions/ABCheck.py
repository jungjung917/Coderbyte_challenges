"""
Have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.
"""
def ABCheck(str_input):
    for i in range(0,len(str_input)-4):
        if str_input[i] == "a" and str_input[i+4] == "b":
	    return "true"
    return "false"
	
        
print ABCheck("Laura sobs")
#print ABCheck( "after badly")
