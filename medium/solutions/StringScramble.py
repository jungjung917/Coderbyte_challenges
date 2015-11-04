"""
the function StringScramble(str1,str2) take both parameters being passed and return the string true if a portion of str1 characters can be rearranged to match str2, otherwise return the string false. For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will not be entered with the parameters. 
"""
def StringScramble(str1,str2):
    for letter in str2.lower():
    	if letter not in str1.lower():
	    return "false"
    return "true"
print StringScramble("cdore","coder")
print StringScramble("ctiye","colrd")
