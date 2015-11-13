"""
Using the Python language, have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are. 
"""
def SwapCase(str_input):
#    return str_input.swapcase()
    str_out =""
    for letter in str_input:
	if letter in "abcdefghijklmnopqrstuvwxyz":
	    str_out = str_out + letter.upper()
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	    str_out = str_out + letter.lower()
	else:
	    str_out = str_out + letter
    return str_out
print SwapCase("Hello-LOL")
print SwapCase("Sup DUDE!!?")
